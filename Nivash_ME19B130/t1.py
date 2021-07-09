import numpy as np
import random
z=np.random.rand(100)
y=np.random.randint(2,size=100)
O=0
for i in range(100):
	O=(-1/100)*(y[i]*np.log2(z[i]) + (1-y[i])*np.log2(1-z[i]))+O
print(O)
