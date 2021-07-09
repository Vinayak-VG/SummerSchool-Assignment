import numpy as np

y1 = np.random.rand(100,)

y2 = np.random.randint(low=0, high=2, dtype=int, size=(100,))

result = y2 * np.log2(y1) + (1-y2) * np.log2(1-y1)

o = - (np.sum(result))/100

print(o)