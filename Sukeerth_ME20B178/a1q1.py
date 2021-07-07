n = 100

import numpy as np
import math

y_hat = np.random.rand(n) # This variable represents y hat
y = np.random.randint(0, 2, (n))

O = 0
for i in range(0,n):
    O = O - (y[i]*math.log2(y_hat[i]) + (1-y[i])*math.log2(1-y_hat[i]))
O = O/n

print("Value of n taken:", n)
print("Value of O obtained is:", O)
