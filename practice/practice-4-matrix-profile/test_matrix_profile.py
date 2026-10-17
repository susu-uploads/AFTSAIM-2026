"""Run with: python -m unittest test_matrix_profile."""
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
from stumpy import config

from modules.mp import compute_mp
from modules.motifs import top_k_motifs
from modules.discords import top_k_discords
from modules.meter_swapping_detection import meter_swapping_detection


def reference_profile(a, m, b=None, zone=0):
    """Direct normalized distances, independent of STUMPY's profile algorithm."""
    self_join = b is None
    b = a if self_join else b
    left = np.lib.stride_tricks.sliding_window_view(a, m)
    right = np.lib.stride_tricks.sliding_window_view(b, m)
    profile = np.full(len(left), np.inf)
    for i, x in enumerate(left):
        if not np.isfinite(x).all():
            continue
        for j, y in enumerate(right):
            if not np.isfinite(y).all() or (self_join and abs(i - j) <= zone):
                continue
            sx, sy = np.std(x), np.std(y)
            if sx == 0 or sy == 0:
                distance = 0.0 if sx == sy else np.sqrt(m)
            else:
                distance = np.linalg.norm((x - x.mean()) / sx - (y - y.mean()) / sy)
            profile[i] = min(profile[i], distance)
    return profile


class MatrixProfileTests(unittest.TestCase):
    def setUp(self):
        self.rng = np.random.default_rng(42)

    def test_self_join_zones_and_missing_windows(self):
        a = self.rng.normal(size=30)
        a[12] = np.nan
        original = config.STUMPY_EXCL_ZONE_DENOM
        for zone in [0, 2, 5]:
            with self.subTest(zone=zone):
                actual = compute_mp(a, 5, zone)
                np.testing.assert_allclose(actual['mp'], reference_profile(a, 5, zone=zone), atol=1e-7)
                self.assertEqual(actual['mp'].dtype, np.dtype('float64'))
                self.assertEqual(actual['mpi'].dtype, np.dtype('int64'))
                valid = np.isfinite(actual['mp'])
                self.assertTrue(np.all(np.abs(np.flatnonzero(valid) - actual['mpi'][valid]) > zone))
                self.assertEqual(config.STUMPY_EXCL_ZONE_DENOM, original)

    def test_cross_join_and_constants(self):
        a = self.rng.normal(size=18)
        b = self.rng.normal(size=23)
        a[:5] = 1
        b[:5] = 2
        b[-1] = np.nan
        actual = compute_mp(a, 5, ts2=b)
        np.testing.assert_allclose(actual['mp'], reference_profile(a, 5, b), atol=1e-7)
        for i, j in enumerate(actual['mpi']):
            self.assertGreaterEqual(j, 0)
            distance = reference_profile(a[i:i+5], 5, b[j:j+5])[0]
            self.assertAlmostEqual(actual['mp'][i], distance, places=7)

    def test_invalid_inputs_and_restoration_on_failure(self):
        for series, m in [(np.zeros((3, 4)), 3), (np.zeros(5), 2), (np.zeros(5), 6)]:
            with self.assertRaises(ValueError):
                compute_mp(series, m)
        original = config.STUMPY_EXCL_ZONE_DENOM
        with patch('modules.mp.stumpy.stump', side_effect=RuntimeError('test')):
            with self.assertRaises(RuntimeError):
                compute_mp(np.arange(10.0), 4, 4)
        self.assertEqual(config.STUMPY_EXCL_ZONE_DENOM, original)

    def test_extrema_exclusions_and_input_preservation(self):
        profile = {'mp': np.array([.1, .4, np.nan, np.inf, .1, .5, .2, .6, .8, .2]),
                   'mpi': np.array([4, 6, -1, -1, 0, 1, 9, 0, 0, 6]), 'excl_zone': 1}
        before = profile['mp'].copy()
        self.assertEqual(top_k_motifs(profile, 20)['indices'], [[0, 4], [6, 9]])
        discords = top_k_discords(profile, 20)
        self.assertEqual(discords['indices'], [8, 5, 1])
        self.assertTrue(np.isfinite(discords['distances']).all())
        np.testing.assert_array_equal(profile['mp'], before)
        invalid = {'mp': np.array([np.nan, np.inf]), 'mpi': np.array([-1, -1]), 'excl_zone': 1}
        for finder in [top_k_motifs, top_k_discords]:
            self.assertEqual(finder(invalid, 3)['indices'], [])
            self.assertEqual(finder(profile, 0)['indices'], [])

    def test_known_swap(self):
        first = self.rng.normal(size=20)
        second = self.rng.normal(size=20)
        heads = {'H_1': pd.DataFrame(first), 'H_2': pd.DataFrame(second)}
        tails = {'T_1': pd.DataFrame(second), 'T_2': pd.DataFrame(first)}
        found = meter_swapping_detection(heads, tails, [1, 2], 5)
        self.assertNotEqual(found['i'], found['j'])
        self.assertLess(found['score'], 1e-5)

    def test_swap_score_denominator_and_all_pairs(self):
        heads = {f'H_{i}': pd.DataFrame([i]) for i in [1, 2, 3]}
        tails = {f'T_{i}': pd.DataFrame([i]) for i in [1, 2, 3]}
        values = {(1, 1): 10, (2, 2): 2, (3, 3): 4,
                  (1, 2): 1, (1, 3): 4, (2, 1): 1, (2, 3): 3,
                  (3, 1): 2, (3, 2): 3}

        def fake(a, m, ts2):
            return {'mp': np.array([values[int(a[0]), int(ts2[0])], np.inf])}

        with patch('modules.meter_swapping_detection.compute_mp', side_effect=fake) as mock:
            found = meter_swapping_detection(heads, tails, [1, 2, 3], 3)
        self.assertEqual(mock.call_count, 9)
        self.assertEqual((found['i'], found['j']), (1, 2))
        self.assertAlmostEqual(found['score'], 1 / 10.001)


if __name__ == '__main__':
    unittest.main()
