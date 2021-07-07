import numpy as np


def cross(y, y_p):
    return(np.sum(-1/100 * (y * np.log2(y_p) + (1 - y) * np.log2(1 - y_p))))

y_p = np.random.uniform(0,1, size = 100)
y = np.random.randint(2, size = 100)
print(cross(y, y_p))
