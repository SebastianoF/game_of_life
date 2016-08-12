import numpy as np


ind = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def cell_degree(x, y, x_dim, y_dim, arr):
    a = np.sum([arr[(x + i) % x_dim, (y + j) % y_dim] for i, j in ind])
    return a
