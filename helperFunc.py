import numpy as np


def display(pairs):
    n, _ = pairs.shape
    for i in range(n):
        print("(", pairs[i][0], ",", pairs[i][1], ")")
    print()


def dist(A, B):
    d = np.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)
    return d


def minDist(d1, A1, B1, d2, A2, B2):
    if d1 <= d2:
        return d1, A1, B1
    else:
        return d2, A2, B2
