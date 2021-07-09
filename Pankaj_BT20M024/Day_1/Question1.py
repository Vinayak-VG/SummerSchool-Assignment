import numpy as np
import math

n = 100

y = np.random.randint(2,size=n)
y_cap = np.random.rand(n)

print(y)
print(y_cap)

sum=0

for i in range(n):
  sum = sum + y[i] * math.log2(y_cap[i]) + (1 - y[i]) * math.log2(1 - y_cap[i])

O = sum * (-1 / n)

print(O)