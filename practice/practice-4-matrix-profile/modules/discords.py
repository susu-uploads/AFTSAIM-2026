import numpy as np

from modules.utils import *


def top_k_discords(matrix_profile: dict, top_k: int = 3) -> dict:
    """
    Find the top-k discords based on matrix profile

    Parameters
    ---------
    matrix_profile: the matrix profile structure
    top_k: number of discords

    Returns
    --------
    discords: top-k discords (indices, distances to its nearest neighbor and the nearest neighbors indices)
    """
 
    discords_idx = []
    discords_dist = []
    discords_nn_idx = []

    # INSERT YOUR CODE

    mp = np.asarray(matrix_profile['mp'], dtype=float).copy()
    mpi = np.asarray(matrix_profile['mpi'])
    mp[~np.isfinite(mp) | (mpi < 0) | (mpi >= len(mp))] = -np.inf
    for _ in range(top_k):
        if not len(mp):
            break
        index = int(np.argmax(mp))
        if not np.isfinite(mp[index]):
            break
        discords_idx.append(index)
        discords_dist.append(float(mp[index]))
        discords_nn_idx.append(int(mpi[index]))
        apply_exclusion_zone(mp, index, matrix_profile['excl_zone'], -np.inf)

    return {
        'indices' : discords_idx,
        'distances' : discords_dist,
        'nn_indices' : discords_nn_idx
        }
