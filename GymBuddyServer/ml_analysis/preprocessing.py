import numpy as np

# DTW

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def dynamic_time_warping(seq1, seq2, dist_func=euclidean_distance):
    n, m = len(seq1), len(seq2)
    dtw_matrix = np.zeros((n + 1, m + 1))
    dtw_matrix[0, 1:] = np.inf
    dtw_matrix[1:, 0] = np.inf

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = dist_func(seq1[i - 1], seq2[j - 1])
            dtw_matrix[i, j] = cost + min(dtw_matrix[i - 1, j], dtw_matrix[i, j - 1], dtw_matrix[i - 1, j - 1])

    return dtw_matrix[n, m]

# Example usage:
seq1 = np.array([1, 3, 4, 9, 8, 2, 1])
seq2 = np.array([1, 5, 3, 8, 9, 4, 1])

distance = dynamic_time_warping(seq1, seq2)
print("DTW distance:", distance)