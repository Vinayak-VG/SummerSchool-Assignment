import numpy as np
import math as ma

n=int(input())
y_hat=np.random.rand(n)
y=np.random.randint(0,2,(n))
O=0;

for i in range(0,n):
    O=O+y[i]*ma.log(y_hat[i],2)+(1-y[i])*ma.log(1-y_hat[i],2)

O=-1*O/n
print(O)
