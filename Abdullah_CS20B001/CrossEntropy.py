import numpy as np

n = 100

y = np.random.randint(0, 2, n)
y_cap = np.random.rand(n)

ans1 = - np.mean(y * np.log2(y_cap) + (1 - y) * np.log2(1 - y_cap))
print(ans1)