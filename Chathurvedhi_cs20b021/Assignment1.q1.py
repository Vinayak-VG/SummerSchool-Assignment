
n = 20

import numpy as np
import math

y_hat = np.random.rand(n) # This variable represents y hat
y = np.random.randint(0, 2, (n))

val = 0
for i in range(n):
    val = val - (y[i]*math.log2(y_hat[i]) + (1-y[i])*math.log2(1-y_hat[i]))
val = val/n

print("Value of n taken:", n)
print("y_hat=",y_hat)
print("y=",y)
print("Value of O obtained is:", val)