import numpy as np
import math
n=5

y=np.random.randint(0,2,n)
y_cap=np.random.rand(100)

O=0
for i in range(n):
    O=O+(y[i]*math.log(y_cap[i],2)+(1-y[i])*math.log(1-y_cap[i],2))

O=(O/n)*(-1)
print(O)