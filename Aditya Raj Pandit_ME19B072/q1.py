import math

import numpy as np

dimension = 10
y_hat = np.random.rand(dimension)
y = np.random.randint(0, 2, dimension)

o = np.sum(-(1/dimension)*((y * np.log2(y_hat)) + ((1 - y) * np.log2(1 - y_hat))))

print(o)
