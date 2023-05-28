import random
import numpy as np
from helperFunc import display
from findClosestPair import findClosestPair


def generateElements(matrix, n):
    lower_bound = -10
    upper_bound = 10
    for i in range(n):
        for j in range(2):
            random_int = random.randint(lower_bound, upper_bound)
            matrix[i, j] = random_int

    return matrix


n = 10

pairs = np.empty((n, 2), dtype=int)
pairs = generateElements(pairs, n)

display(pairs)

X = np.array(sorted(pairs, key=lambda p: (p[0], p[1])))
Y = np.array(sorted(pairs, key=lambda p: (p[1], p[0])))

display(X)
display(Y)

findClosestPair(X, Y)
