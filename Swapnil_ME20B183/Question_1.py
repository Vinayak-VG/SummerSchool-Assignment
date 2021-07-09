#!/usr/bin/python3
# coding: utf-8

# In[246]:


import numpy as np

n=int(input("Enter the value of n"))
#n=4  # number of elements in the array

y = np.random.randint(0,2,(n))  
# y array contains elements either 0 or 1

y_hat = np.random.rand(n) 
#y_hat contains elements between 0 and 1 [0,1)


S=0 
for i in range(0,n):
    c = y[i]*np.log2(y_hat[i]) +  (1-y[i])*np.log2(1-y_hat[i])
    S+=c

# S stores the value of sum which will be mulbtiplied with (-1/n) to get O

O = (S/n)*(-1)
#O

print("y = ",y)
print("y_hat = ",y_hat)
print("O = ",O)

