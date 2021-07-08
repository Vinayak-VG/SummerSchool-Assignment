import numpy as np

n = 100
y_cap = np.random.rand(n)
y = np.random.randint(0, 2, n)

array = y * np.log2(y_cap) + (1 - y) * np.log2(1 - y_cap)
O = (-1/n)* np.sum(array)

print(O)
