# Author: Sai Shashank GP
# Date last modified: 06-07-2021
# Purpose: Using Cross-Entropy function for given inputs

# importing useful libraries

import numpy as np

# defining required functions

def Oi(y, y_cap):
    '''
    
    This function finds the summation terms list for each element of y and y_cap
    
    '''
    O_list = []
    length = len(y)
    for i in range(length):
        val = (y[i]*np.log(y_cap[i])) + ((1-y[i])*np.log(1-y_cap[i]))
        O_list.append(val)
    return O_list

def sum_list(l):
    '''
    
    This function sums up the terms in a list
    
    '''
    s = 0
    for val in l:
        s += val
    return s

# writing inputs for Cross-Entropy function as lists

Y = list(np.random.rand(100))
y = list(np.random.randint(0, 2, 100))

# printing answer

answerlist = Oi(y, Y)
answer_1 = -0.01*sum_list(answerlist)
print(answer_1)
