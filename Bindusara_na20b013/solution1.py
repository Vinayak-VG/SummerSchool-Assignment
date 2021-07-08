import numpy as np

n=5
y=np.random.randint(0,2,n)
y_hat=np.random.rand(n)
n = 7
y_hat = np.array([0.45, 0.10, 0.99, 0.32, 0.78, 0.81,0.27])
y = np.array([1, 0, 1, 1, 1, 0, 0])
ones=np.ones(n)
x=np.array(n)
x=(y*(np.log2(y_hat)))+((ones-y)*(np.log2(ones-y_hat)))
O = np.array(n)
O=(-1/n)*(np.sum(x,axis=0))
print(O)
