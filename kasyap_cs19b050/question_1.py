import numpy as np
import math

y2=np.random.rand(100)
y1=np.random.randint(2,size=100)
y3=1-y1
y4=np.log2(y2)
y5=np.log2(1-y2)
y6=y1*y4+y3*y5
x=sum(y6)
x/=100
x*=-1
print(x)
