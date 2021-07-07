import numpy as np
import random

'''
Q1: Create two vectors 𝑦 and 𝑦̂ having the same dimensions, where 𝑦̂ should
consist of random numbers between [0,1) and 𝑦 should contain 0𝑠 and
1𝑠, for example, 𝑦=[0,1,1,0,1,0,0,1,...,1].**

Where n = 100, is the total number of elements in y and 𝑦̂
Note: The expression O, which you have computed is actually a
Cross-Entropy loss function used in machine learning for classification
tasks which tells us how bad or good the model is performing, if O is large
then the model is performing worst and vice versa.
'''
def Cross_entropy(y,yhat):
  loss = y*np.log2(yhat) + (1-y)*np.log2(1-yhat)
  CE = -np.sum(loss)/len(loss)
  return CE

yhat = np.random.rand(100)
y = np.random.randint(2, size=len(yhat))
Cross_entropy(y,yhat)

'''
**2 . Write a Python class to find a pair of elements (indices of the two
numbers) from a given array whose sum equals a specific target
number.**
>Note: There will be multiple solutions, so create a dictionary where the
keys represent just S.No(1,2,3,4…..) and the value corresponding to
the key represents the indices of the two numbers
For example: Input: numbers= [10,20,10,40,50,60,70], target=50
Output: {1: [0, 3], 2: [2, 3], 3: [3, 0], 4: [3, 2]}
'''
class SUMFINDER:
  
  def __init__(self, target, array):
    self.target= target
    self.array= array

  def find(self):
    out = {}
    n= 1
    for i in range(len(self.array)):
      for j in range(len(self.array)):

        if self.array[i]+self.array[j] == self.target:
          out[n]=[i,j]
          n+=1

    return out
  
