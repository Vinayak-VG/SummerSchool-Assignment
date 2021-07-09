#import numpy as np
class dict:
    def __init__(self,a,t):
        self.array=a
        self.target=t

    def show(self):
        length=len(self.array)
        temp_Dict={}
        output_Dict={}
        idx=1
        for i in range(length):
            temp_Dict[(self.array)[i]]=[]
        for i in range(length):
            temp_Dict[(self.array)[i]].append(i)

        for num in temp_Dict:
            if self.target-num in temp_Dict:
                for i in range(len(temp_Dict[num])):
                    for y in temp_Dict[self.target-num]:
                        output_Dict[idx]=[temp_Dict[num][i],y]
                        idx=idx+1
        print(output_Dict)
 







array=list(map(int,input("enter the elements of the array : ").strip().split()))
target=int(input("enter the target number : "))
dictionary=dict(array,target)
dictionary.show()
