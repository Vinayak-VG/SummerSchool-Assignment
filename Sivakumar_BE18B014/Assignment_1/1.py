from math import log, log2
import numpy as np

n = 1000
y1 = np.rint(np.random.rand(n))  # Random 0s, 1s (Uniform)
y2 = np.random.rand(n)  # Random numbers in [0, 1) (Uniform)


def cross_entropy(y1, y2):
    return (-1 / n) * (np.sum(y1*np.log2(y2) + (1 - y1)*np.log2(1 - y2)))


print(cross_entropy(y1, y2))
