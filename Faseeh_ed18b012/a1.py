import numpy as np
import random

n = int(input())
y = np.zeros((n,))
y_hat = np.random.rand(n)
print(y_hat)
rand_num = 0
count = 0
while(rand_num < 8):
    rand_num = random.randint(0,10)
    y[int((rand_num/10)*(n-1))] = 1
    count += 1
#print(count)
#print(y)
n= 7
y_hat = np.array([0.45, 0.10, 0.99, 0.32, 0.78, 0.81, 0.27]) 
y = np.array([1, 0, 1, 1, 1, 0, 0])
O = y*np.log2(y_hat) + (1-y)*np.log2(1-y_hat)
print(-O.mean())