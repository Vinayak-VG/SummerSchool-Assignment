import random
import math

def operationO(n):
    y = []
    for i in range(0,n):
        y.append(random.random())
    print(y)

    z= []
    for i in range(0,n):
        z.append(random.randint(0,1))
    print(z)

    sum = 0
    for i in range(0,n):
        sum += (z[i]*math.log(y[i],2) + (1-z[i])*math.log(1-y[i],2))
    result = -sum/n
    print(result)
user_input = int(input('Enter an integer:'))
answer = operationO(user_input)




