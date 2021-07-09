# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:19:36 2021

@author: Rishitha
"""

import numpy as np
array_list=eval(input("Enter a list of numbers (array elements):"))
array=np.asarray(array_list)
sum_pairs=float(input("Enter the required sum of pairs of elements in list:"))

class sumation:
    index_dict={}
    @classmethod
    def pairs(cls,arr,N):
        count=0
        n=len(arr)
        for i in range(n):
            index=np.where(arr==(N-arr[i]))
            for j in index[0]:
                count+=1
                cls.index_dict[count]=[i,j]
        print(cls.index_dict)
sumation.pairs(array,sum_pairs)                
                
