
# question 1 

import numpy as np 

d = 100 # dimension of each array 
y_hat = np.random.rand(1,d)
y = np.random.randint(2, size=d)

"""
Test Case 1
d = 5
y_hat = np.array([0.32, 0.56, 0.71, 0.14, 0.57])
y = np.array([1, 0, 1, 1, 0])
"""

O = -1/d * np.sum(y*np.log2(y_hat)+(1-y)*np.log2(1-y_hat))
print(O)