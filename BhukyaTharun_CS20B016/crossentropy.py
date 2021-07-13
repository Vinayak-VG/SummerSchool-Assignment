import numpy as np 

n = 100
#https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.rand.html#numpy.random.RandomState.rand
#np.random.rand(n) creates 1 dimension of size n with range [0,1) 
y_hat = np.random.rand(n)
#print(y_hat)

#https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.randint.html#numpy.random.RandomState.randint
#np.random.randint(0,2,n) creates random n integer numbers from [0,2) 
y = np.random.randint(0,2,n)
#print(y)

#https://numpy.org/doc/stable/reference/generated/numpy.log2.html#numpy.log2
#np.log2(x) calculates array of log2 of each element of x
#https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean
#np.mean(x) calculates mean of array of x
O = -np.mean(y*np.log2(y_hat) + (1-y)*np.log2(1-y_hat))
print(O)
