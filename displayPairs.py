def display(pairs):
    n, _ = pairs.shape
    for i in range(n):
        print("(", pairs[i][0], ",", pairs[i][1], ")")
    print()
