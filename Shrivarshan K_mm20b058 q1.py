import numpy as np
import math
n=input();
n=int(n);
if n==0:
   print("invalid input")
else:
  ycap=np.random.rand(n)
  y=np.random.randint(0,2,(n))
  sum=0.0
  for i in range(n)
   sum+=y[i]*(math.log2(ycap[i]))+(1-y[i])*(math.log2(1-ycap[i]))
   output=sum/(-n)
   print(output)