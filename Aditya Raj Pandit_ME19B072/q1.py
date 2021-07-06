import math

import numpy as np

dimension = 100
y_hat = np.random.rand(dimension)
y = np.random.randint(0, 2, dimension)

summation = 0.0
for i in range(dimension):
    summation += ((y[i] * math.log2(y_hat[i])) + ((1 - y[i]) * math.log2(1 - y_hat[i])))

o = -summation * (1 / dimension)

print(o)
