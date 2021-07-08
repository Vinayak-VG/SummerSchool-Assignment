import numpy as np

N = 100

y_hat = np.random.rand(N)
y = np.random.randint(low = 0, high = 2 , size = (n))
O = -np.sum(y * np.log2(y_hat) + (1 - y) * np.log2(1 - y_hat))/n
print(O)
