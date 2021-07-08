import numpy as np
import math

n=100

y=np.random.rand(1,size=n)
ycap=np.randon.randit(2,size=n)

array1 = np.multiply(y,np.log2(ycap))+np.multiply(1-y,np.log2(1-ycap))
print(np.sum(array1)/(-n))


