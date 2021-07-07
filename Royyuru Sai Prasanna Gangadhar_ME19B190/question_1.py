import numpy as np
import math as m
n = int(input('Enter integer number:'))
y1= np.random.rand(n)
y = np.random.randint(0,2,n)
print(y)
print(y1)
o = 0
for i in range(0,n):
    o = o+ ((y[i]*(m.log(y1[i],2)))+((1-y[i])*m.log(1-y1[i],2)))

o_avg = (-1/n)*o
print("Cross-Entropy is ",o_avg)