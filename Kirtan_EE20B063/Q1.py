import numpy as np
import math 
n = 100
y_hat = np.random.rand(n)
y = np.random.randint(0,2,(n))
temp = 0
for i in range(n):
    temp = temp - (y[i]*math.log2(y_hat[i]) + (1-y[i])*math.log2(1-y_hat[i]))

temp = temp/n
print(temp)
