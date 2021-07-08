import numpy as np
y1=np.array(np.random.randint(2,size=100))
y2=np.array(np.random.rand(100))
y3=np.log2(1-y2)
y2=np.log2(y2)
result=(y1*y2)+((1-y1)*y3);
cross_entropy = -1*(np.sum(result))/100
print(cross_entropy);
