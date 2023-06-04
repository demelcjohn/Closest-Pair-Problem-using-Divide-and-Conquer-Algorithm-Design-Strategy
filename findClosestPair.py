import numpy as np
from helperFunc import dist
from helperFunc import minDist


def findClosestPair(X):
    n, _ = X.shape

    if (n == 2):
        return dist(X[0], X[1]), X[0], X[1]
    if (n == 3):
        dmin, A, B = minDist(dist(X[0], X[1]), X[0],
                             X[1], dist(X[0], X[2]), X[0], X[2])
        dmin, A, B = minDist(dist(X[2], X[1]), X[2], X[1], dmin, A, B)
        return dmin, A, B

    mid = n//2

    dl, Al, Bl = findClosestPair(X[:mid])
    dr, Ar, Br = findClosestPair(X[mid:])
    d, A, B = minDist(dl, Al, Bl, dr, Ar, Br)

    S = []
    dmin = d
    for i in range(mid):
        if X[mid][0]-d <= X[i][0]:
            for j in range(mid, n):
                if X[mid][0]+d >= X[j][0]:
                    dmin, A, B = minDist(
                        dmin, A, B, dist(X[i], X[j]), X[i], X[j])

    d = min(d, dmin)

    return d, A, B
