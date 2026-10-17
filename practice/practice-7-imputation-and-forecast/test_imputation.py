"""Run with: python -m unittest test_imputation."""
import tempfile
import unittest
from pathlib import Path

import numpy as np
import torch
from sklearn.preprocessing import MinMaxScaler

from modules.imputation import add_nan, hot_deck, rolling_window, iterative_svd, masked_metrics
from modules.models import LinearModel, TimeAE, training_mask, train_model, reconstruct


torch.set_num_threads(4)


class ImputationTests(unittest.TestCase):
    def test_missing_fraction_copy_and_reproducibility(self):
        x = np.arange(40.).reshape(10, 4)
        for fraction in [0, .25, 1]:
            damaged, mask = add_nan(x, fraction)
            self.assertEqual(mask.shape, x.shape)
            self.assertEqual(mask.sum(), int(x.size * fraction))
            np.testing.assert_array_equal(np.isnan(damaged), mask)
            np.testing.assert_array_equal(damaged[~mask], x[~mask])
            np.testing.assert_array_equal(x, np.arange(40.).reshape(10, 4))
            np.testing.assert_array_equal(mask, add_nan(x, fraction)[1])
        for fraction in [-.1, 1.1, np.nan]:
            with self.assertRaises(ValueError):
                add_nan(x, fraction)

    def test_hot_deck_original_right_neighbor_and_end(self):
        x = np.array([np.nan, 2., np.nan, np.nan, 7., np.nan])
        np.testing.assert_array_equal(hot_deck(x), [2, 2, 7, 7, 7, 7])
        self.assertTrue(np.isnan(x[0]))
        with self.assertRaises(ValueError):
            hot_deck([np.nan, np.nan])

    def test_windows_include_last_and_keep_splits_separate(self):
        x = np.arange(30.).reshape(15, 2)
        windows = rolling_window(x, 4)
        self.assertEqual(windows.shape, (12, 4, 2))
        np.testing.assert_array_equal(windows[-1], x[-4:])
        train = rolling_window(x[:8], 4, 4)
        test = rolling_window(x[8:], 4, 4)
        self.assertLess(train.max(), test.min())
        scaler = MinMaxScaler().fit(x[:8])
        np.testing.assert_array_equal(scaler.data_max_, x[7])
        self.assertTrue((scaler.transform(x[8:]) > 1).all())

    def test_svd_recovers_rank_one_and_preserves_observations(self):
        x = np.outer(np.arange(1., 11), np.arange(1., 7))
        damaged, mask = add_nan(x, .15)
        initial = np.where(mask, np.nanmean(damaged, axis=0), damaged)
        recovered = iterative_svd(damaged, rank=1)
        np.testing.assert_array_equal(recovered[~mask], x[~mask])
        self.assertTrue(np.isfinite(recovered).all())
        self.assertLess(np.mean((recovered[mask] - x[mask]) ** 2),
                        np.mean((initial[mask] - x[mask]) ** 2))
        with self.assertRaises(ValueError):
            iterative_svd(np.full((4, 3), np.nan), rank=1)

    def test_metrics_ignore_observed_values(self):
        x = np.array([1., 2., 3., 4.])
        mask = np.array([True, False, True, False])
        reconstructed = np.array([2., 999., 4., 999.])
        result = masked_metrics(x, reconstructed, mask)
        self.assertEqual(result['MSE'], 1)
        self.assertEqual(result['RMSE'], 1)
        self.assertEqual(result['MAE'], 1)

    def test_models_shape_masks_and_one_training_epoch(self):
        torch.manual_seed(42)
        x = np.arange(120., dtype=np.float32).reshape(12, 5, 2) / 120
        x[:, 1, 1] = np.nan
        selected = training_mask(torch.tensor(x), torch.Generator().manual_seed(42))
        self.assertEqual(int(selected.sum()), int(np.isfinite(x).sum() * .25))
        self.assertFalse(selected[torch.isnan(torch.tensor(x))].any())
        for model in [LinearModel(5, 2), TimeAE(5, 2)]:
            with self.subTest(model=type(model).__name__):
                self.assertEqual(model(torch.zeros(3, 5, 2)).shape, (3, 5, 2))
                truth = np.linspace(0, 1, 40).reshape(4, 5, 2)
                missing, mask = add_nan(truth, .25)
                with tempfile.TemporaryDirectory() as temp:
                    history, elapsed = train_model(model, x, missing, truth,
                                                   Path(temp)/'test.pt', epochs=1)
                self.assertTrue(np.isfinite(history['train_mse']).all())
                self.assertTrue(np.isfinite(history['validation_mse']).all())
                self.assertGreater(elapsed, 0)
                recovered = reconstruct(model, missing)
                np.testing.assert_array_equal(recovered[~mask], truth[~mask])
                self.assertTrue(np.isfinite(recovered).all())


if __name__ == '__main__':
    unittest.main()
