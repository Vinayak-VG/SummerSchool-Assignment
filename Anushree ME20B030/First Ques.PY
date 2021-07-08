n=100

import numpy as np

import math

y=np.random.randint(0,2,(1,100)) #randomly generating integers 0 and 1
yc=np.random.rand(1,100) #randomly generating values belonging to[0,1)

sum=0

for i in range (0,n):

     sum=sum- (((y[0,i] * math.log(yc[0,i],2)) + ((1-y[0,i]) * math.log(1-yc[0,i], 2)))/n)



print(sum) #printing value of the given expression