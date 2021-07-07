import numpy as np
import math
ycap=np.random.rand(100)
y=np.random.random_integers(0,1,100)
s=0.0

for i in range (100):
    s=s+(y[i]*math.log(ycap[i],2)+(1-y[i])*math.log(1-ycap[i],2))
o=(-1/100)*s
print(o)
