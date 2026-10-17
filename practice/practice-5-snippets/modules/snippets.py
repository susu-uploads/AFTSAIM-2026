import numpy as np
import matplotlib.pyplot as plt


def regime_labels(snippets, n):
    """Restore one label per window start from STUMPY's half-open regimes."""
    m = len(snippets[0][0])
    labels = np.full(n - m + 1, -1, dtype=int)
    for value, start, stop in snippets[5]:
        if not 0 <= value < len(snippets[0]) or not 0 <= start < stop <= len(labels):
            raise ValueError("Invalid snippet regime")
        if np.any(labels[start:stop] != -1):
            raise ValueError("Snippet regimes overlap")
        labels[start:stop] = value
    if np.any(labels == -1):
        raise ValueError("Snippet regimes do not cover all window starts")
    return labels


def align_binary_labels(labels, reference):
    """Choose identity or flipped snippet IDs by agreement with a reference."""
    labels, reference = np.asarray(labels), np.asarray(reference)
    if labels.shape != reference.shape or labels.ndim != 1:
        raise ValueError("Label arrays must have the same one-dimensional shape")
    if not np.isin(labels, [0, 1]).all() or not np.isin(reference, [0, 1]).all():
        raise ValueError("Only binary labels are supported")
    if np.count_nonzero(labels != reference) > np.count_nonzero(1 - labels != reference):
        return 1 - labels
    return labels.copy()


def majority_vote(labels):
    """Vote over the three aligned binary gyroscope axes."""
    labels = np.asarray(labels)
    if labels.ndim != 2 or labels.shape[0] != 3 or not np.isin(labels, [0, 1]).all():
        raise ValueError("Expected three equally sized binary label arrays")
    return (labels.sum(axis=0) >= 2).astype(int)


def profile_change(areas):
    """Compute Change for successive cumulative profile areas; k=1 is undefined."""
    areas = np.asarray(areas, dtype=float)
    if areas.ndim != 1 or not np.isfinite(areas).all() or np.any(areas < 0):
        raise ValueError("Profile areas must be a finite non-negative vector")
    change = np.full(len(areas), np.nan)
    with np.errstate(divide='ignore', invalid='ignore'):
        change[1:] = areas[:-1] / areas[1:] - 1
    return change


# Визуализация сниппетов
def plot_snippets(ts, snippets):
    with plt.rc_context(
        {
            "lines.linewidth": 2,
            "font.size": 24,
        }
    ):
        fig, (ax_main, ax_labels) = plt.subplots(
            2, figsize=(16, 6), gridspec_kw={"height_ratios": [16, 2]}
        )
        color_cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

        ax_main.plot(ts, color="gray")

        m = len(snippets[0][0])
        snippets_indices = snippets[1]
        for i, snippet_start in enumerate(snippets_indices):
            snippet_end = snippet_start + m
            ax_main.plot(
                np.arange(snippet_start, snippet_end),
                ts[snippet_start:snippet_end],
                c=color_cycle[i],
                label=f"Snippet {i}: {snippets[3][i]:.2f}",
            )

        labels = regime_labels(snippets, len(ts))
        offset = m // 2
        ax_labels.imshow([labels], cmap="tab10", aspect="auto", vmin=0,
                         vmax=len(color_cycle) - 1, interpolation='nearest',
                         extent=(offset - 0.5, offset + len(labels) - 0.5, 0, 1))

        ax_main.set_xlim(0, len(ts))
        ax_labels.set_xlim(0, len(ts))
        ax_labels.axis("off")
        ax_main.legend(prop={"size": 16}, loc="upper right")
        plt.tight_layout()
        plt.show()
    return ax_main
