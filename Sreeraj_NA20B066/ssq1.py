import numpy as np
s=0
y_hat = np.random.random(5)
y=np.array([1,0,1,1,0])
O=sum(-(1/5)*((y*np.log2(y_hat))+((1-y)*np.log2(1-y_hat))))
print(O)