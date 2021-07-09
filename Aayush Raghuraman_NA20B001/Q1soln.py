#Cross entropy loss function
import numpy as np
import random as rd
sum=0
n=rd.randint(4,100)
y_hat=np.random.rand(n,)
y=np.random.randint(0,2,(n,))
arr1=np.log2(y_hat)
arr2=np.log2(1-y_hat)
for i in range(0,n):
    sum=sum+y[i]*arr1[i]+(1-y[i])*arr2[i]
print(-1*sum/n)

