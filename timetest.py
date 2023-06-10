import csv
import random
import numpy as np
from bruteforce import bruteforce
from helperFunc import display
from findClosestPair import findClosestPair
from rep import representation
import timeit


def generateElements(matrix, n):
    lower_bound = -10
    upper_bound = 10
    for i in range(n):
        for j in range(2):
            random_int = random.randint(lower_bound, upper_bound)
            matrix[i, j] = random_int

    return matrix


data = [
    ['n', 'divAndConTime', 'bruteForceTime']
]

for i in range(3,100):
    row = []
    n = i
    row.append(n)
    pairs = np.empty((n, 2), dtype=int)
    pairs = generateElements(pairs, n)

    display(pairs)

    X = np.array(sorted(pairs, key=lambda p: (p[0], p[1])))

    start_time = timeit.default_timer()
    d, A, B = findClosestPair(X)
    end_time = timeit.default_timer()
    runtime = end_time - start_time
    row.append(runtime)

    start_time = timeit.default_timer()
    d1,A1,B1 = bruteforce(X)
    end_time = timeit.default_timer()
    runtime = end_time - start_time
    row.append(runtime)

    data.append(row)

    csv_file = 'data.csv'

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)

