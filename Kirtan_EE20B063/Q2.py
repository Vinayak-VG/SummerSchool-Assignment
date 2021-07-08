import numpy as np 
import math
class Kirtan:
    arr = [10,20,10,40,50,60,70] 
    target = 50
    def f(self):
        dic = {}
        count = 1
        
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):
                if (self.arr[i]+self.arr[j] == self.target):
                    dic[count] = [i,j]
                    count = count+1
        
        print(dic)
o = Kirtan()
o.f()

    