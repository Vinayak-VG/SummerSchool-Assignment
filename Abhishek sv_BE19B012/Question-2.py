import math
import numpy as np


n = [10,20,30,40,50,60,70.80]
Target = 80
x=1


Output = { }

for i in range(7):
    for j in range(7):
        if n[i]+n[j] == Target : 

            Output[x]= [i,j]
            x = x+1
        
print(Output)