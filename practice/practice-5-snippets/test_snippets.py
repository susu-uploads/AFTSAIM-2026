"""Run with: python -m unittest test_snippets."""
import unittest
from unittest.mock import patch

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from modules.snippets import (
    regime_labels, align_binary_labels, majority_vote, profile_change, plot_snippets,
)


def example_snippets(regimes):
    return (np.zeros((2, 3)), np.array([0, 3]), np.zeros((2, 5)),
            np.array([.6, .4]), np.array([10., 5.]), np.array(regimes))


class SnippetTests(unittest.TestCase):
    def test_half_open_regimes_and_no_tail_padding(self):
        result = example_snippets([[0, 0, 2], [1, 2, 4], [0, 4, 5]])
        np.testing.assert_array_equal(regime_labels(result, 7), [0, 0, 1, 1, 0])

    def test_invalid_regimes(self):
        for regimes in [[[0, 0, 2]], [[0, 0, 3], [1, 2, 5]],
                        [[0, -1, 5]], [[2, 0, 5]], [[0, 0, 6]]]:
            with self.subTest(regimes=regimes), self.assertRaises(ValueError):
                regime_labels(example_snippets(regimes), 7)

    def test_binary_permutation_and_identity_tie(self):
        reference = np.array([0, 0, 1, 1])
        np.testing.assert_array_equal(align_binary_labels(1-reference, reference), reference)
        np.testing.assert_array_equal(align_binary_labels([0, 1, 0, 1], reference), [0, 1, 0, 1])
        with self.assertRaises(ValueError):
            align_binary_labels([12, 13], [0, 1])

    def test_majority_after_alignment(self):
        y = np.array([0, 0, 1, 1])
        x = align_binary_labels([1, 1, 0, 0], y)
        z = align_binary_labels([0, 1, 1, 1], y)
        np.testing.assert_array_equal(majority_vote([x, y, z]), y)
        with self.assertRaises(ValueError):
            majority_vote([x, y])

    def test_change_formula(self):
        change = profile_change([100, 50, 40])
        self.assertTrue(np.isnan(change[0]))
        np.testing.assert_allclose(change[1:], [1, .25])
        self.assertTrue(np.isinf(profile_change([1, 0])[1]))
        self.assertTrue(np.isnan(profile_change([0, 0])[1]))
        with self.assertRaises(ValueError):
            profile_change([1, np.inf])

    def test_plot_shows_only_window_centers(self):
        result = example_snippets([[0, 0, 2], [1, 2, 4], [0, 4, 5]])
        with patch('matplotlib.pyplot.show'):
            ax = plot_snippets(np.arange(7.), result)
        image = ax.figure.axes[1].images[0]
        self.assertEqual(image.get_array().shape, (1, 5))
        np.testing.assert_allclose(image.get_extent(), [.5, 5.5, 0, 1])
        plt.close(ax.figure)


if __name__ == '__main__':
    unittest.main()
