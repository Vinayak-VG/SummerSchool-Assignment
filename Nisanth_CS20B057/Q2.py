import numpy
class findpair:
    def __init__(self,arr,n,target):
        self.arr=arr
        self.target=target
        self.arrsize=n
    def findthepairs(self):
        self.pairs={}
        k=1
        for i in range(n):
            for j in range(i+1,n):
                if(self.arr[i]+self.arr[j]==self.target):
                    self.pairs[k]=[i,j]
                    k+=1
    def returnpairs(self):
        return self.pairs

n=int(input())
tar=int(input())
arr=list()
for i in range(n):
    arr.append(int(input()))
solve=findpair(arr,n,tar)
solve.findthepairs()
print(solve.returnpairs())

