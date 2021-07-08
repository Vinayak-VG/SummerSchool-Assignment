import numpy as np

n=100
y_cap=np.random.rand(100)
y=np.random.randint(0,2,(100))
b=0
for i in range(n):
   b=b+y[i]*np.log2(y_cap[i])+(1-y[i])*np.log2(1-y_cap[i]) 
c=(-1/n)*b   
print (c)