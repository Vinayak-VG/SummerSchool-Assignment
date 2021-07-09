
import numpy as np
n = 100
y = np.random.randint(0,2,(n))
y_hat = np.random.rand(n)
k = np.sum((y*np.log2(y_hat))+((1-y)*np.log2(1-y_hat)))
o = -k/n
print("Answers is ",o)