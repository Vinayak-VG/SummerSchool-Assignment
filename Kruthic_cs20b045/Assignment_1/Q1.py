# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IL51j5D7rNG4_Yf_DrCleGMyitI1g-dF
"""

import numpy as np
import math 

n = 100
y_cap = np.random.rand(n)
y = np.random.randint(0, 2, n)

O = 0
for i in range(n):
    O += y[i]*math.log2(y_cap[i]) + (1-y[i])*math.log2(1-y_cap[i])  
    
O /= -n
print(O)