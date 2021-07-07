# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:54:53 2021

@author: PiyushBhujbal
"""

target  = int(input())

numbers = list(map(int,input().split()))

print(numbers)

class MyClass:
    
    def show(self,n,array):
        ans = []
        
        for i in range(0,len(array)):
            for j in range(0,len(array)):
                if n == array[i]+array[j]:
                    ans.append([[i,j]])
        
        dic = dict(zip(range(1,len(ans)+1),ans))
        print(dic)
       
C = MyClass()
C.show(target,numbers)