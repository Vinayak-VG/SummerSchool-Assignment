import numpy as np

n=5
y=np.random.randint(0,2,n)
y_hat=np.random.rand(n)
ones=np.ones(n)
x=np.array(n)
x=(y*(np.log2(y_hat)))+((ones-y)*(np.log2(ones-y_hat)))
O = np.array(n)
O=(-1/n)*(np.sum(x,axis=0))
print(O)
