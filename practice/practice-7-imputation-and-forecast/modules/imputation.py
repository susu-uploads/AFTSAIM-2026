"""Masking, analytical imputation, and evaluation for practice 7."""
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def add_nan(x, percent=0.25, seed=42):
    """Hide exactly floor(x.size * percent) finite values without mutating x."""
    data = np.array(x, dtype=float, copy=True)
    if not 0 <= percent <= 1 or not np.isfinite(data).all():
        raise ValueError("Expected a finite array and a missing fraction between 0 and 1")
    mask = np.zeros(data.size, dtype=bool)
    chosen = np.random.default_rng(seed).choice(data.size, int(data.size * percent), replace=False)
    mask[chosen] = True
    mask = mask.reshape(data.shape)
    data[mask] = np.nan
    return data, mask


def hot_deck(series):
    """Use the first original observation to the right, then the last to the left."""
    result = np.array(series, dtype=float, copy=True)
    if result.ndim != 1 or np.isinf(result).any():
        raise ValueError("Expected a one-dimensional series without infinities")
    observed = np.flatnonzero(np.isfinite(result))
    if not len(observed):
        raise ValueError("Hot-Deck needs at least one observed value")
    missing = np.flatnonzero(np.isnan(result))
    donors = np.minimum(np.searchsorted(observed, missing), len(observed) - 1)
    result[missing] = result[observed[donors]]
    return result


def rolling_window(data, window=100, step=1):
    """Return all full windows; never create a window across a split boundary."""
    data = np.asarray(data)
    if data.ndim not in (1, 2) or not 1 <= window <= len(data) or step < 1:
        raise ValueError("Expected a 1D/2D array, a valid window, and a positive step")
    windows = np.lib.stride_tricks.sliding_window_view(data, window, axis=0)
    if data.ndim == 2:
        windows = windows.swapaxes(1, 2)
    return windows[::step].copy()


def iterative_svd(matrix, rank=2, max_iter=100, tolerance=1e-5):
    """Iteratively reconstruct missing entries, holding all observations fixed."""
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2 or not 1 <= rank <= min(matrix.shape) or np.isinf(matrix).any():
        raise ValueError("Expected a matrix without infinities and a valid rank")
    missing = np.isnan(matrix)
    if np.any(np.all(missing, axis=0)):
        raise ValueError("Each SVD column needs at least one observed value")
    result = np.where(missing, np.nanmean(matrix, axis=0), matrix)
    if not missing.any():
        return result
    for _ in range(max_iter):
        previous = result[missing].copy()
        u, singular, vt = np.linalg.svd(result, full_matrices=False)
        reconstructed = (u[:, :rank] * singular[:rank]) @ vt[:rank]
        result[missing] = reconstructed[missing]
        relative = np.linalg.norm(result[missing] - previous) / max(np.linalg.norm(previous), 1e-12)
        if relative < tolerance:
            break
    return result


def masked_metrics(truth, restored, mask):
    """Score only hidden values, in the original data scale."""
    truth, restored, mask = np.asarray(truth), np.asarray(restored), np.asarray(mask)
    if truth.shape != restored.shape or truth.shape != mask.shape or mask.dtype != bool:
        raise ValueError("Data and boolean mask must have the same shape")
    if mask.sum() < 2 or not np.isfinite(restored[mask]).all():
        raise ValueError("At least two finite reconstructed targets are required")
    expected, predicted = truth[mask], restored[mask]
    mse = float(mean_squared_error(expected, predicted))
    return {'MSE': mse, 'RMSE': float(np.sqrt(mse)),
            'MAE': float(mean_absolute_error(expected, predicted)),
            'R2': float(r2_score(expected, predicted))}
