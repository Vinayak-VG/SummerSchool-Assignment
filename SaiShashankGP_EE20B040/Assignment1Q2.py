'''
Author: Sai Shashank GP
Date last modified: 07-07-2021
Purpose: To find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Sample input: 10 20 10 40 50 60 70
Sample ouput: {1: [0, 3], 2: [2, 3], 3: [3, 0], 4: [3, 2]}
'''

# importing useful libraries

import numpy as np
import random

# creating a random numbers list and target number

mean = uniform(0, 10)
std_dev = uniform(0, 10)
numbers = list((np.random.rand(100)*std_dev)+mean)    
targetnumber = uniform(0, 100)        


def Checkcondition(N, T):
    '''
    
    This function checks the required condition for each and every possile pair and returns the list of pairs of required indices.
    
    '''
    finallist = []
    len_N = len(N)
    for i in range(len_N):
        for j in range(len(N)):
            if N[i]+N[j] == T:
                answer = [i, j]
                finallist.append(answer)
            else:
                continue
    return finallist
            
    
class FindTargetIndices:
    '''
    
    This class contains to find indices of a pair of elements in a given list which add up to the given target number.
    
    '''
    target_indices = Checkcondition(numbers, targetnumber)
    
    def show(self):
        dict_target_indices = {}
        for i in range(len(self.target_indices)):
            dict_target_indices[i+1] = self.target_indices[i]
        print(dict_target_indices)

answer_2 = FindTargetIndices()
answer_2.show()
