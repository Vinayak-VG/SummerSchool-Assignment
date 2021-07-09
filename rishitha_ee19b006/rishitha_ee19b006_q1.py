# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:35:42 2021

@author: Rishitha
"""
import numpy as np
n=int(input("Enter the number of elements in y ,y_cap (both are of same size):"))
#vector containing random numbers between [0,1)
y_cap=np.random.rand(n)
#vector containing 0's and 1's
y=np.random.randint(0,2,(n))
#y_cap=np.array([0.45,0.10,0.99,0.32,0.78,0.81,0.27])
#y=np.array([1,0,1,1,1,0,0])
O_i=(-1/n)*(y*np.log2(y_cap)+(1-y)*np.log2((1-y_cap)))
O=np.sum(O_i)
print("Value of O:",O)
