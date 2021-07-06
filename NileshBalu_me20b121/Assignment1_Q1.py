import numpy as np
import math
x=np.random.rand(10,10)
y=np.random.randint(0,2,(10,10))
ct = 0.0
for i in range(10):
    for j in range(10):
        ct += y[i,j]*(math.log2(x[i,j])) + (1-y[i,j])*(math.log2(1-x[i,j]))
O = ct/(-100)
print (O)