from helperFunc import dist


def findClosestPair(X, Y):
    n, _ = X.shape

    if (n == 2):
        return dist(X[0], X[1])
    if (n == 3):
        return min(dist(X[0], X[1]), dist(X[0], X[2]).dist(X[2], X[1]))

    mid = n//2

    dl = findClosestPair(X[:(n//2)][:], Y)
    dr = findClosestPair(X[(n//2):][:], Y)
    d = min(dl, dr)

    S = []
    for i in range(n):
        if ((X[n//2][0]-d <= Y[0]) and (X[n//2][0]+d >= Y[0])):
            S = S.append(Y[i])
