# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:13:38 2021

@author: Chekuri Viroopaksh
"""

import random,math
n=100
y=[random.choice([0,1]) for _ in range(n)]
y_cap=[round(random.random(),3) for _ in range(n)]
O=0
for i in range(n):
    O+=(y[i]*(math.log2(y_cap[i]))+((1-y[i])*math.log2(1-y_cap[i])))
O=-1*(O/n)
print("y =",y)
print("y^ =",y_cap)
print("O =",O)