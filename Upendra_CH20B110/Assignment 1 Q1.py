import numpy as np
import math
n = 100
y = np.random.randint(0,2,n) # n random numbers from {0,1} 
y_hat = np.random.rand(n) # n random numbers from [0,1)
print(y)
print(y_hat)
sum = 0.00
for i in range(n):
  sum = sum + y[i]*math.log2(y_hat[i]) + (1-y[i])*math.log2(1-y_hat[i])
O = sum*(-1/n) # Computing Cross Entropy Loss function
print(O)