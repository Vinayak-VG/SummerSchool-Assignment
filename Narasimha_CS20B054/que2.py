import numpy as np

dic = {}


class Data :
 def __init__():
 
         self.inp =  input().split(' ') 
         self.target = int(input())


 def __init__(self,target,inpu_arr):
         self.inp = inpu_arr
         self.target = target

         
 def solve(self) :
  
         t = len(self.inp)
         
         self.count = 0
         for i in range(t - 1):
               for j in range (i + 1,t):
                    if (self.inp[i] + self.inp[j] == self.target ):
                           dic[self.count] = list([i,j])
                           self.count = self.count + 1


       
#input order
#<target>
#<inp_0> < > <inp_1> .....<inp_(n - 1)>


target = int(input())
inpu_arr = [int(x) for x in input().split()]

Output =  Data(target,inpu_arr)
Output.solve()

print(dic)

 


