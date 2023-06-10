from helperFunc import dist


def bruteforce(X):
    n,_ = X.shape
    min = 10**10
    for i in range(n):
        for j in range(n):
            if i!=j:
                d = dist(X[i],X[j])
                if d<min:
                    min = d
                    points = (X[i],X[j])
    return min,points[0],points[1]
