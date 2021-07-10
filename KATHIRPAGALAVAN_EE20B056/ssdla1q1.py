import numpy as np
import math as m
O=0.0
order=int(input('order:'))
ycap=np.random.rand(order)
y=np.random.randint(0,2,(order,))
for i in range(order):
    O=O-(1/order)*( y[i]*m.log2(ycap[i]) + (1-y[i])*m.log2(1-ycap[i]) )
print(O)