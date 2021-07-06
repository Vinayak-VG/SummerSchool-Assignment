import numpy as np
import random
import math

w = []


y = np.arange(100)

for n in range(100):
    y[n] = random.randint(0,1)
    
z = np.arange(100)    

for n in range(100):
    z[n] = random.randint(1,999)
    w.append(float(z[n]/1000))
    
O = 0
for n in range(100):
    k = ((y[n]*math.log(w[n],2))+(1-y[n])*(math.log(1-w[n],2)))
    O = O+k
    
O = O/(-100)

    
print(O) 







  
  
    

