import numpy as np
import math
n = 100
y_cap = np.random.rand(n)
y = np.random.randint(0,2,n)
k = 0
for i in range(n):
    k = k + y*math.log(y_cap,2) + (1 - y)*(math.log((1 - y_cap) , 2))
O = -(k/n)
O = np.mean(y*math.log2(y_cap) + (1 - y)*(math.log2(1 - y_cap)))

print(O)

n = int(input("Enter number of elements : "))

numbers = []
for i in range(n):
    numbers.append(int(input()))
    
target = int(input("Enter target : "))
