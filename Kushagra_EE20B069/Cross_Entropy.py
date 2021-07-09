import numpy as np
N = int(input("Enter value of N : "))
y_cap = np.random.rand(N)
y = np.random.randint(0,2, size = (N))
O = (-1) * (1/N) * np.sum(y * np.log2(y_cap) + (1 - y) * np.log2(1-y_cap))
print(O)