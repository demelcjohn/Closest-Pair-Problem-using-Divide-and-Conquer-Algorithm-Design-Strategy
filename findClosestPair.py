import numpy as np
from helperFunc import dist


def findClosestPair(X):
    n, _ = X.shape

    if (n == 2):
        return dist(X[0], X[1])
    if (n == 3):
        return min(dist(X[0], X[1]), dist(X[0], X[2]), dist(X[2], X[1]))

    mid = n//2

    dl = findClosestPair(X[:mid])
    dr = findClosestPair(X[mid:])
    d = min(dl, dr)

    S = []
    dmin = d
    for i in range(mid):
        if X[mid][0]-d <= X[i][0]:
            for j in range(mid, n):
                if X[mid][0]+d >= X[j][0]:
                    dmin = min(dmin, dist(X[i], X[j]))

    d = min(d, dmin)

    return d
