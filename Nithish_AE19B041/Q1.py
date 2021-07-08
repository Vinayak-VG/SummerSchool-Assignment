import numpy as np
import random
import math
y1=np.random.rand(100)
y=np.random.randint(2,size=100)
O=0
for i in range(100):
	O=O-(y[i]*math.log(y1[i],2)+(1-y[i])*math.log(1-y1[i],2))/100
print(O)

	
