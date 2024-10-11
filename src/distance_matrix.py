from scipy.spatial import distance
import numpy as np


def calculate_euclidean_distance(vec1, vec2):
    return distance.euclidean(vec1, vec2)


def create_distance_matrix(frequencies):
    all_keys = sorted(set().union(*[freq.keys() for freq in frequencies.values()]))

    freq_matrix = np.zeros((len(frequencies), len(all_keys)))

    for i, (record_id, freq) in enumerate(frequencies.items()):
        for j, key in enumerate(all_keys):
            freq_matrix[i, j] = freq.get(key, 0)

    dist_matrix = np.zeros((len(frequencies), len(frequencies)))
    for i in range(len(frequencies)):
        for j in range(i, len(frequencies)):
            dist = calculate_euclidean_distance(freq_matrix[i], freq_matrix[j])
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist

    return dist_matrix, list(frequencies.keys()), all_keys
