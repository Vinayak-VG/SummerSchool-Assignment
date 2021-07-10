# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 10:08:57 2021

@author: CIBI
"""
n=int(input())
target=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
c=0
output={}
for i in range(len(l)):
    for j in range(len(l)):
        if(i!=j):
            out=[]
            if(l[i]+l[j]==target):
                out.append(i)
                out.append(j)
                c=c+1
                output[c]=out
                