import numpy as np
import math
import random


n = int(input("Enter the number: "))
# if user inputs the vectors y and y_cap

#y_cap = list(map(float, input("Enter the numbers between 0-1: ").split()))
#y = list(map(int, input("Enter the integers(0,1 only): ").split()))

# if we create vectors y and y_cap by random values
y_cap = list(map(lambda x: round(x, 2), np.random.rand(n)))
y = np.random.choice([0, 1], n)

print('y_cap = ', y_cap)
print("y = ", y)
sum = 0
for i in range(n):
    sum += y[i]*math.log(y_cap[i], 2) + (1-y[i])*(math.log(1-y_cap[i], 2))
output = -(sum/n)
print("O = ", round(output, 5))
