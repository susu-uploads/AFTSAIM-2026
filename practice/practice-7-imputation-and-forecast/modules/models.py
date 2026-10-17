"""Linear and GRU imputers based on the assignment architectures."""
from pathlib import Path
from time import perf_counter

import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader


class LinearModel(nn.Module):
    def __init__(self, size_subsequent=100, dim=10):
        super().__init__()
        self.window, self.features = size_subsequent, dim
        size = size_subsequent * dim
        self.network = nn.Sequential(
            nn.Flatten(), nn.Linear(size, 250), nn.LeakyReLU(),
            nn.Linear(250, 250), nn.LeakyReLU(),
            nn.Linear(250, 250), nn.LeakyReLU(),
            nn.Linear(250, size), nn.Tanh(),
        )

    def forward(self, x):
        return self.network(x).reshape(-1, self.window, self.features)


class TimeAE(nn.Module):
    def __init__(self, size_subsequent=100, dim=10):
        super().__init__()
        self.window = size_subsequent
        self.encoder = nn.GRU(dim, 100, batch_first=True)
        self.to_latent = nn.Linear(size_subsequent * 100, 100)
        self.from_latent = nn.Linear(100, size_subsequent * 100)
        self.decoder = nn.GRU(100, dim, batch_first=True)
        self.activation = nn.LeakyReLU()

    def forward(self, x):
        encoded, _ = self.encoder(x)
        latent = self.activation(self.to_latent(self.activation(encoded).flatten(1)))
        decoded = self.activation(self.from_latent(latent)).reshape(-1, self.window, 100)
        output, _ = self.decoder(decoded)
        return self.activation(output)


def training_mask(x, generator):
    """Hide 25% of the known elements, excluding pre-existing missing values."""
    observed = torch.isfinite(x)
    selected = torch.zeros(x.numel(), dtype=torch.bool)
    candidates = torch.nonzero(observed.flatten(), as_tuple=True)[0]
    count = int(len(candidates) * 0.25)
    if count:
        selected[candidates[torch.randperm(len(candidates), generator=generator)[:count]]] = True
    return selected.reshape(x.shape)


def reconstruct(model, windows, batch_size=64):
    """Predict in batches while preserving observed values exactly."""
    model.eval()
    output = []
    with torch.no_grad():
        for batch in DataLoader(torch.as_tensor(windows, dtype=torch.float32), batch_size=batch_size):
            predicted = model(torch.nan_to_num(batch, nan=0.0))
            output.append(torch.where(torch.isnan(batch), predicted, batch).numpy())
    return np.where(np.isnan(windows), np.concatenate(output), windows)


def train_model(model, train, validation, validation_truth, checkpoint, epochs=100, patience=10):
    """Train on artificial masks; choose the best state using validation only."""
    checkpoint = Path(checkpoint)
    checkpoint.parent.mkdir(parents=True, exist_ok=True)
    loader = DataLoader(torch.as_tensor(train, dtype=torch.float32), batch_size=64,
                        shuffle=True, generator=torch.Generator().manual_seed(42))
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    generator = torch.Generator().manual_seed(43)
    val_missing = np.isnan(validation)
    if not val_missing.any():
        raise ValueError("Validation must contain held-out missing values")
    best, stale, history = np.inf, 0, []
    started = perf_counter()
    for epoch in range(epochs):
        model.train()
        squared_error, elements = 0.0, 0
        for batch in loader:
            masked = training_mask(batch, generator)
            if not masked.any():
                continue
            inputs = batch.clone()
            inputs[masked] = 0.0
            predicted = model(torch.nan_to_num(inputs, nan=0.0))
            loss = ((predicted[masked] - batch[masked]) ** 2).mean()
            if not torch.isfinite(loss):
                raise ValueError("Training loss became non-finite")
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            count = int(masked.sum())
            squared_error += loss.item() * count
            elements += count
        if not elements:
            raise ValueError("No training targets were masked")
        recovered = reconstruct(model, validation)
        val_mse = float(np.mean((recovered[val_missing] - validation_truth[val_missing]) ** 2))
        if not np.isfinite(val_mse):
            raise ValueError("Validation loss became non-finite")
        history.append({'epoch': epoch + 1, 'train_mse': squared_error / elements,
                        'validation_mse': val_mse, 'elapsed_s': perf_counter() - started})
        if val_mse < best:
            best, stale = val_mse, 0
            torch.save(model.state_dict(), checkpoint)
        else:
            stale += 1
        pd.DataFrame(history).to_csv(checkpoint.with_suffix('.csv'), index=False)
        print(f'{checkpoint.stem}: epoch {epoch+1}, train={squared_error/elements:.6f}, '
              f'validation={val_mse:.6f}, elapsed={perf_counter()-started:.1f}s', flush=True)
        if stale >= patience:
            break
    model.load_state_dict(torch.load(checkpoint, map_location='cpu', weights_only=True))
    return pd.DataFrame(history), perf_counter() - started
