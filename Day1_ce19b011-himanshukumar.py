from random import random

import numpy as np
n=int(input("enter size"))
y_hat=np.random.rand(n)
y=np.random.randint(2,size=n)
y_dash=np.log2(y_hat)
y__dash=np.log2(1-y_hat)
o=((y*y_dash)+((1-y)*y__dash))*(-1/n)
print(o.sum())



# *******QN 2 **********
arr=[]
x=input("enter numbers seperated by space tab for array")
for i in x.split():
    arr.append(int(i))
target=int(input("enter number for which you wanna get desired indices"))
dict={}
arr1=[[j,k] for j in range(len(arr)) for k in range(len(arr)) if arr[j]+arr[k]==target]
print(arr1)
for k in range(len(arr1)):
    dict[k+1]=arr1[k]
print(dict)


