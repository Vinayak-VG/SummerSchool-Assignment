import numpy as np
import math

y_cap=np.random.rand(100)
y1=np.random.randint(2,size=100)
y3=1-y1
y4=np.log2(y_cap)
y5=np.log2(1-y_cap)
y6=y1*y4+y3*y5
out=sum(y6)
out/=100
out*=-1
print(out)
