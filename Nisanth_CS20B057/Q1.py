import numpy as np
import math
y_cap=np.random.rand(100)
y=np.random.randint(0,2,(100))
o=0.0
for i in range(100):
  o+= y[i] * math.log(y_cap[i],2) + ( 1 - y[i] ) * math.log(y_cap[i],2)
o/=-100
print(o)