# -*- coding: utf-8 -*-
"""CVI_Ass1_Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L-62kXgVZrkh_dBs3-9Pgw0GbZldZbgp

Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
"""

import numpy as np

class findpair:
  def __init__(self, array, target):
    self.array=array;
    self.target=target;
    self.pair();
  
  def pair(self):
    self.dic={};
    self.c=1;
    for i in range(len(self.array)):
      for j in range(len(self.array)):
        if self.array[i]+self.array[j]==target:
          self.dic[self.c]=[i,j];
          self.c=self.c+1;

  def show(self):
    print(self.dic)


#array=[input()]  #doesnot work. sigh
#target=int(input())

array=[10,20,10,40,50,60,70]
target=50

findpair(array,target).show()

