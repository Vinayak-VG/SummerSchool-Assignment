import numpy as np

n = 100
y_hat = np.random.rand(n,)
y = np.random.randint(0, 2, n)
result = (-1/n)*np.sum(y*np.log2(y_hat) + (1 - y)*(1 - np.log2(1 - y_hat)))
print("Cross Entropy Loss = ",result)
