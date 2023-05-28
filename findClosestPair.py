from helperFunc import dist


def findClosestPair(X, Y):
    n, _ = X.shape

    if (n == 2):
        return dist(X[0], X[1])
    if (n == 3):
        return min(dist(X[0], X[1]), dist(X[0], X[2]).dist(X[2], X[1]))
