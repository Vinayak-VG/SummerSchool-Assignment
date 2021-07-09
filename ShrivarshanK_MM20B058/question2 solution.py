import numpy as np
class findpairele:
  c={}
  def _init_(self,arr,n,sum):
   key=0
   for i in range(n):
    for j in range(n):
     if arr[i]+arr[j]==sum:
       key+=1
       self.c[key]=[i,j]
  def show(self):
    print(self.c)
sum=input()
sum=int(sum)
n=input()
n=int(n)
arr=np.array([])
for i in range(n):
  x=input()
  x=int(x)
  arr=np.append(arr,x)
s1=findpairele(arr,n,sum)
s1.show()
 