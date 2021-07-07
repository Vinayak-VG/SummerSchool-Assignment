class TargFind:
    def __init__(self,array=[14, 15, 25, 36, 17, 18, 22, 21],target=39):
        self.sno=0
        self.output={}
        for m in range(len(array)):
            for n in range(len(array)):
                if int(array[m])+int(array[n])==target:
                    self.sno=self.sno+1
                    self.output[self.sno]=[m,n]
        print(self.output)

print('Enter space separated numbers for the array:')
a=input().split()
print('Enter the target value:')
t=int(input())

out=TargFind(a,t)