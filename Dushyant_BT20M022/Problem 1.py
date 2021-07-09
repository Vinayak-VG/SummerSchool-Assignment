import numpy as np
import math as ma

#defining given parameters
n=100
y2 = np.random.random_sample(n)
y1 = np.random.randint(2, size=n)

#checking purposes
#print(y1)
#print(y2)

#equation
def exp(x1,x2):
    val=(x1*(ma.log(x2,2)))+((1-x1)*ma.log(1-x2,2))
    return val

#summation
res=0
for i in range(n):
    res=res+exp(y1[i],y2[i])

#final result
O=-(res/n)
print('The value of Output is',O)