arr=[10,20,10,40,50,60,70]
target=50
numdict={}
ctr=1
class pair:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        s=self.a+self.b
        return s
for i in range(7):
    for j in range(7):
        obj=pair(arr[i],arr[j])
        if(obj.add()==target):
           numdict[ctr]=[i,j]
           ctr+=1
print(numdict)