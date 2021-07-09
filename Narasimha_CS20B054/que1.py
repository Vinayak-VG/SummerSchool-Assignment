import numpy as np
N = 100



y = np.random.rand(N)
y1 = np.random.randint(0,2,N)


en = 0.00
for i in range(N):
   en = en - (1/N)*(y1[i]*np.log2(y[i]) + (1 - y[i])*np.log2(1 - y[i]))
 



print("Cross- Entropy = ",en)
