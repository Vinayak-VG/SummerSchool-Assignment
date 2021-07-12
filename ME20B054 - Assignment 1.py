# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 04:56:56 2021

@author: HP
"""

class elements_pair:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    def add88(self,i,j) :
        return self.arr[i]+self.arr[j]
    
    def show_dict(self):
        print(len(self.arr))
        dictionary = {}
        a=1
        for i in range(0,len(self.arr)):
            for j in range(0,len(self.arr)):
                if i!=j and self.add88(i,j)==self.target:
                    dictionary[a]=[i,j]
                    a=a+1
        print(dictionary)
        
q = elements_pair([12,17,15,18,13,11],30)   
q.show_dict()    
        
              
        