import numpy as np

from modules.utils import z_normalize


def ED_distance(ts1: np.ndarray, ts2: np.ndarray) -> float:
    """
    Calculate the Euclidean distance

    Parameters
    ----------
    ts1: the first time series
    ts2: the second time series

    Returns
    -------
    ed_dist: euclidean distance between ts1 and ts2
    """
    
    ed_dist = np.sqrt(np.sum((ts1 - ts2) ** 2))

    return ed_dist


def norm_ED_distance(ts1: np.ndarray, ts2: np.ndarray) -> float:
    """
    Calculate the normalized Euclidean distance

    Parameters
    ----------
    ts1: the first time series
    ts2: the second time series

    Returns
    -------
    norm_ed_dist: normalized Euclidean distance between ts1 and ts2s
    """

    ts1, ts2 = ts1 - ts1[0], ts2 - ts2[0]
    n = len(ts1)
    std1, std2 = np.std(ts1), np.std(ts2)
    if std1 == 0 or std2 == 0:
        norm_ed_dist = ED_distance(z_normalize(ts1), z_normalize(ts2))
    else:
        correlation = (np.dot(ts1, ts2) - n * np.mean(ts1) * np.mean(ts2)) / (n * std1 * std2)
        norm_ed_dist = np.sqrt(abs(2 * n * (1 - np.clip(correlation, -1, 1))))

    return norm_ed_dist


def DTW_distance(ts1: np.ndarray, ts2: np.ndarray, r: float = 1) -> float:
    """
    Calculate DTW distance

    Parameters
    ----------
    ts1: first time series
    ts2: second time series
    r: warping window size
    
    Returns
    -------
    dtw_dist: DTW distance between ts1 and ts2
    """

    dtw_dist = 0

    n = ts1.size
    radius = ((n / 100) * r) * 100
    indices = np.arange(n)
    first_row = np.ceil(np.interp(indices, [0, n - 1], [-radius, n - radius - 1]))
    last_row = np.floor(np.interp(indices, [0, n - 1], [radius, n + radius - 1]))
    first_row = first_row.clip(0, n - 1).astype(int)
    last_row = last_row.clip(0, n - 1).astype(int)
    cost = np.full((n + 1, n + 1), np.inf)
    cost[0, 0] = 0
    for j in range(1, n + 1):
        for i in range(first_row[j - 1] + 1, last_row[j - 1] + 2):
            cost[i, j] = (ts1[i - 1] - ts2[j - 1]) ** 2 + min(
                cost[i - 1, j], cost[i, j - 1], cost[i - 1, j - 1]
            )
    dtw_dist = float(cost[n, n])

    return dtw_dist
