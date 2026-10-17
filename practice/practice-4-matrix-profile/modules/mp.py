import numpy as np
import pandas as pd
import math

import stumpy
from stumpy import config


def compute_mp(ts1: np.ndarray, m: int, exclusion_zone: int = None, ts2: np.ndarray = None):
    """
    Compute the matrix profile

    Parameters
    ----------
    ts1: the first time series
    m: the subsequence length
    exclusion_zone: exclusion zone
    ts2: the second time series

    Returns
    -------
    output: the matrix profile structure
            (matrix profile, matrix profile index, subsequence length, exclusion zone, the first and second time series)
    """
    
    # INSERT YOUR CODE

    ts1 = np.asarray(ts1, dtype=np.float64)
    ts2 = None if ts2 is None else np.asarray(ts2, dtype=np.float64)
    if ts1.ndim != 1 or (ts2 is not None and ts2.ndim != 1):
        raise ValueError("Time series must be one-dimensional")
    if not isinstance(m, (int, np.integer)) or not 3 <= m <= len(ts1):
        raise ValueError("Window length must be an integer between 3 and the series length")
    if ts2 is not None and m > len(ts2):
        raise ValueError("Window length exceeds the second series length")
    if exclusion_zone is None:
        exclusion_zone = math.ceil(m / config.STUMPY_EXCL_ZONE_DENOM)
    if not isinstance(exclusion_zone, (int, np.integer)) or exclusion_zone < 0:
        raise ValueError("Exclusion zone must be a non-negative integer")

    denominator = config.STUMPY_EXCL_ZONE_DENOM
    try:
        # STUMPY exposes the self-join radius through this global setting.
        config.STUMPY_EXCL_ZONE_DENOM = m / exclusion_zone if exclusion_zone else np.inf
        mp = stumpy.stump(ts1, m, T_B=ts2, ignore_trivial=ts2 is None)
    finally:
        config.STUMPY_EXCL_ZONE_DENOM = denominator

    return {'mp': np.asarray(mp[:, 0], dtype=np.float64),
            'mpi': np.asarray(mp[:, 1], dtype=np.int64),
            'm' : m,
            'excl_zone': exclusion_zone,
            'data': {'ts1' : ts1, 'ts2' : ts2}
            }
