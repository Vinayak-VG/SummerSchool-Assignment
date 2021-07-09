import numpy as np
import math as m
O=0.0
count=int(input('Input an integer :'))
ycap=np.random.rand(count)
y=np.random.randint(0,2,(count,))
for i in range(count):
    O=O-(1/count)*( y[i]*m.log2(ycap[i]) + (1-y[i])*m.log2(1-ycap[i]) )
print(O)