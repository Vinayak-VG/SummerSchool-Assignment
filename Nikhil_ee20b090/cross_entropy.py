import numpy as np
a=np.random.rand(100)
b=np.random.randint(0,2,(100,))
c=b*np.log2(a)+(1-b)*np.log2(1-a)
o=np.sum(c)/(-100)
print(o)