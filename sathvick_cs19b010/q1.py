import numpy as np

N = 100

y_hat = np.random.rand(N)
y = np.random.randint(0, 2, N)

cross_entropy = (-1/N)*np.sum(y*np.log2(y_hat) + (1 - y)*(1 - np.log2(1 - y_hat)))

print(f"{cross_entropy=}")
