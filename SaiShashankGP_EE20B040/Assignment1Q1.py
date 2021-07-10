'''
Author: Sai Shashank GP
Date last modified: 07-07-2021
Purpose: Using Cross-Entropy function for given inputs
Sample input: 100
Sample output: 1.375263
'''

# importing useful libraries

import numpy as np
import random

# Assigning n to a random positive integer

n = random.randint(1, 1000)

# writing inputs for Cross-Entropy function as lists

Y = np.random.rand(n)
y = np.random.randint(0, 2, n)
O_arr = -1*((y*(np.log2(Y)))+((1-y)*(np.log2(1-Y))))
answer_1 = np.mean(O_arr)

# printing answer

print(answer_1)
