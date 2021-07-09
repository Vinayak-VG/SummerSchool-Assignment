import numpy as np

y_1 = np.random.rand(100)
y = np.random.randint(0,2,[100])

sum = 0
n = len(y)

for i in range(0,n,1):
    sum += y[i]*np.log2(y_1[i]) + (1-y[i])*np.log2(1-y_1[i])

o = -sum/n

print(o)