import matplotlib.pyplot as plt
import math
import random


def calculate(n, w_max, N):
    y = [0 for _ in range(N)]
    x = [i * 0.0001 for i in range(N)]
    w = w_max / n
    for i in range(n):

        w0 = w * (1 + i)
        A = random.random()
        fi = random.random()
        for t in range(N):
            y[t] += A * math.sin(w0 * x[t] + fi)
    return (x, y)


if __name__ == '__main__':
    n = 12
    w_max = 2700
    N = 640

    plt.plot(calculate(n, w_max, N)[0], calculate(n, w_max, N)[1], label = 'n = 12\nw = 2700\nN = 64')
    plt.legend()
    plt.show()

    M = sum(calculate(n, w_max, N)[1]) / N
    D = sum([(element - M) ** 2 for element in calculate(n, w_max, N)[1]]) / (N - 1)

    print(M, D)
