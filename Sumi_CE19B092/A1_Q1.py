import numpy as np

y_hat = np.random.rand(1, 100)
y = np.random.randint(2, size=100)

o = 0

for i in range(0, 100):
    o = o + y[i]*np.log2(y_hat[0][i]) + (1-y[i])*np.log2(1-y_hat[0][i])

o = -1/100*o
print(o)