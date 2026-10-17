import numpy as np

from modules.utils import *


def top_k_motifs(matrix_profile: dict, top_k: int = 3) -> dict:
    """
    Find the top-k motifs based on matrix profile

    Parameters
    ---------
    matrix_profile: the matrix profile structure
    top_k : number of motifs

    Returns
    --------
    motifs: top-k motifs (left and right indices and distances)
    """

    motifs_idx = []
    motifs_dist = []

    # INSERT YOUR CODE

    mp = np.asarray(matrix_profile['mp'], dtype=float).copy()
    mpi = np.asarray(matrix_profile['mpi'])
    zone = matrix_profile['excl_zone']
    available = np.isfinite(mp) & (mpi >= 0) & (mpi < len(mp))
    for _ in range(top_k):
        eligible = np.flatnonzero(available)
        eligible = eligible[available[mpi[eligible]] & (np.abs(eligible - mpi[eligible]) > zone)]
        if not len(eligible):
            break
        index = int(eligible[np.argmin(mp[eligible])])
        neighbor = int(mpi[index])
        motifs_idx.append(sorted([index, neighbor]))
        motifs_dist.append(float(mp[index]))
        apply_exclusion_zone(available, index, zone, False)
        apply_exclusion_zone(available, neighbor, zone, False)

    return {
        "indices" : motifs_idx,
        "distances" : motifs_dist
        }
