import sys

sys.path.append('../')

import signal_generator_lab_1_1.signal_generator as sg
import matplotlib.pyplot as plt


def matexp(signal):
    return sum(signal) / len(signal)


def correlation(signal1, signal2):
    len1 = len(signal1)
    len2 = len(signal2)
    if len1 != len2:
        raise Exception('Length of correlating signals does not match')
    result = [0] * len1
    m1 = matexp(signal1)
    m2 = matexp(signal2)
    for T in range(len1):
        for t in range(len1 - T):
            result[T] += (signal1[t] - m1) * (signal2[t + T] - m2)
        result[T] = result[T] / (len1 - T)
    return result


n = 12
w_max = 2700
N = 640
signal1 = sg.calculate(n, w_max, N)[1]
signal2 = sg.calculate(24, 1200, 640)[1]
plt.plot([i for i in range(N)], correlation(signal1, signal2))
plt.plot([i for i in range(N)], correlation(signal1, signal1))
plt.show()
