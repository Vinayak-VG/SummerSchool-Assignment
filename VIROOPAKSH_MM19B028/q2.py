# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:14:14 2021

@author: Chekuri Viroopaksh
"""

class Pair_Finder:
    def __init__(self,lst,target):
        self.array=lst
        self.target_num=target
        self.matches={}
    def find_matches(self):
        count=1
        d={}
        for i in range(len(self.array)):
            required=self.target_num-self.array[i]
            for j in range(len(self.array)):
                if required==self.array[j]:
                    d[count]=[i,j]
                    count+=1
        self.matches=d
    
pair_obj=Pair_Finder(lst=  [14, 15, 25, 36, 17, 18, 22, 21],target=39)
pair_obj.find_matches()
print(pair_obj.matches)