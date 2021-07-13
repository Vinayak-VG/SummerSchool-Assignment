import math 
import numpy as np
cross_entropy = 100
y_hat = np.random.rand(cross_entropy)
y = np.random.randint(low=0,high=2,size=cross_entropy)
O = -np.sum(y*np.log2(y_hat)+(1-y)*np.log2(1-y_hat))/cross_entropy
print (O)

