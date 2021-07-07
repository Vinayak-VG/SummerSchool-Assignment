import numpy as np
import math as m
y1= np.random.rand(100)
y = np.random.randint(0,2,100)
print(y)
print(y1)
o = 0
for i in range(0,100):
    o = o+ ((y[i]*(m.log(y1[i],2)))+((1-y[i])*m.log(1-y1[i],2)))

o_avg = (-1/100)*o
print("Cross-Entropy is ",o_avg)