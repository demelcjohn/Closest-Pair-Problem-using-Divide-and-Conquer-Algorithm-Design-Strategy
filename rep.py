import matplotlib.pyplot as plt

def representation(pairs,A,B,n):

    x=[]
    y=[]
    for i in range(n):
        x.append(pairs[i][0])
        y.append(pairs[i][1])

    fig, ax = plt.subplots()

    ax.scatter(x, y, color='red', label='Points')

    ax.plot([A[0],B[0]], [A[1],B[1]], color='blue', linestyle='-', label='Line')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Points and Line')

    ax.legend()

    plt.show()
