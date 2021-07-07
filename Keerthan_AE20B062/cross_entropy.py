import numpy as np

y_cap = np.random.rand(100)
y = np.random.randint(0, 2, 100)

cross_entropy = (-1/100)*np.sum(y*np.log2(y_cap) + (1 - y)*(1 - np.log2(1 - y_cap)))

print(cross_entropy)
