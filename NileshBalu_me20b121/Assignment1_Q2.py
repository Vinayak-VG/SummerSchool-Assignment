import numpy as np
class FindPair:
    d={}
    def __init__(self,arr,n,sum):
        key = 0
        for i in range(n):
            for j in range(n):
                if arr[i]+arr[j] == sum:
                    key+=1
                    self.d [key] = [i,j]
    def show(self):
        print(self.d)
S = input("Sum : ")
S = int(S)
N = input("Number of elements : ")
N = int(N)
A = np.array([])
for i in range(N):
    x = input("Element : ")
    x = int(x)
    A = np.append(A,x)
C1 = FindPair(A,N,S)
C1.show()