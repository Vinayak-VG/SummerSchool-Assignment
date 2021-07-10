
n=int(input())
import numpy as np
import math
y = np.random.randint(0,2, n)
x = np.random.rand(n)
print(y)
print(x)

sum = 0
for i in range(n):
  sum += y[i]*math.log2(x[i]) + (1-y[i])*math.log2(1-x[i])

Cross_entropy = -sum/n

print(Cross_entropy)
