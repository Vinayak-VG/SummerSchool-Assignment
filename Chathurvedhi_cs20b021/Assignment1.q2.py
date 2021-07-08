import numpy as np
import math

class cheata:
    num= [10,20,10,40,50,60,70]
    tar=50
    
    def inputs(self):
        print("Numbers=",self.num)
        print("Target=",self.tar)
    
    def solve(self):
        dict1={}
        count=1
        for i in range(len(self.num)):
            for j in range(len(self.num)):
                if(self.num[i]+self.num[j]==self.tar):
                    dict1[count]=[i+1,j+1]
                    count=count+1
        print(dict1)
    
pn=cheata()
pn.inputs()
pn.solve()