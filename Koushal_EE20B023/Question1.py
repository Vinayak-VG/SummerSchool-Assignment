import numpy as np
import math

n = 100
yhat = np.random.rand(n)           # Uniform distribution in [0,1)   # yhat = y^
print(yhat)
y = np.random.randint(2,size = n)   
print(y)
i = 0
O = 0
while(i<100):
    O = O + ( y[i]*(math.log2(yhat[i])) + (1-y[i])*(math.log2(1-yhat[i])) )
    i = i + 1
O = -O/n
print(O)
