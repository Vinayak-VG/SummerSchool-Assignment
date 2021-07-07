import numpy as np
import math

n = 100

y = np.random.randint(2,size=n)
ycap = np.random.rand(n)

print(y)
print(ycap)

finarr = np.multiply(y,np.log2(ycap))+np.multiply(1-y,np.log2(1-ycap))
ans = (np.sum(finarr)/n)*-1

print(ans)