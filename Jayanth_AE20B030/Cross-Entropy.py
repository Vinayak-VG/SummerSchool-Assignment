import numpy as np

n = 100
y_hat = np.random.rand(n)
y = np.random.randint(0, 2, (n,))
arr = y * np.log2(y_hat) + (1 - y) * np.log2(1 - y_hat)
Op = -1 * np.sum(arr) / n
print(Op)
