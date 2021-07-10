# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:13:34 2021

@author: PiyushBhujbal
"""

import numpy as np

N = int(input())

y_hat = np.random.rand(N)

y = np.random.randint(2,size = N)

O = -np.mean(y * np.log2(y_hat) + (1 - y) * np.log2(1 - y_hat))
print(O)