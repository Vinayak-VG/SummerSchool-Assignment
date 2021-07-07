import numpy as np
import math
n = input("Size : ")
n = int(n)
if n == 0:
    print("Invalid input")
else:

    x=np.random.rand(n)
    y=np.random.randint(0,2,(n))
    ct = 0.0
    for i in range(n):
        ct += y[i]*(math.log2(x[i])) + (1-y[i])*(math.log2(1-x[i]))
    O = ct/(-n)
    print (O)