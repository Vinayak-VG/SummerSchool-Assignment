# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:13:38 2021

@author: Chekuri Viroopaksh
"""

import numpy as np
n = 4
y_cap = np.array([0.23, 0.54, 0.61, 0.89])
y = np.array([0, 0, 1, 1])
O = sum( (i*np.log2(j)+(1-i)*np.log2(1-j)) for (i,j) in zip(y,y_cap) ) * (-1/n)
print("y =",y)
print("y^ =",y_cap)
print("O =",O)