import numpy as np
from math import log
n = 100

y = np.random.randint(2, size=n)
y_hat = np.random.rand(n)
y_hat = y_hat - y_hat//1

O = 0.0
for i in range(n):
    O += y[i] * log(y_hat[i], 2) + (1 - y[i]) * log((1 - y_hat[i]), 2)
O *= -1 / n
print(O)
