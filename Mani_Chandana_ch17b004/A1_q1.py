"""
   Written by Mani Chandana at 11:30 pm - July 8, 2021
   
"""

# Cross entropy loss function calculation

import numpy as np

n = 100

# defining yi and yhat
y_i = np.random.randint(2, size = n)
y_hat = np.random.rand(n)

#  cross entropy loss
# 1-y_i gets broadcasted
loss = -1*np.sum( y_i*np.log2(y_hat) + (1-y_i)*np.log2(1-y_hat))/n
print(loss)