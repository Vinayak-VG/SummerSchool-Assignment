import numpy as np
import math as math

n = 100

y = np.random.randint(0,2,size = n)
y_hat = np.random.rand(100,)
temp = 0
for i in range(n):
    temp += (y[i] * math.log(y_hat[i], 2)) + ((1 - y[i]) * math.log((1 - y_hat[i]), 2))
O = (0 - temp)/n
print(O)