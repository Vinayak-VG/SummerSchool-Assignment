import numpy as np

n=100
y_hat = np.random.rand(n)
y = np.ones(n)

O = (-1/n)*sum(y*np.log2(y_hat)+(1-y)*np.log2(1-y_hat))
print(O)