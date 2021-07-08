from sys import argv,exit
from numpy import *
if len(argv) != 2:
    print('\nUsage: %s <input_n_here>' % argv[0])
    exit()

n=int(argv[1])
yhat=[];y=[]
yhat=random.rand(n)
y=random.randint(2,size=n)
O=0
for i in range(n):
    O+=(y[i]*log2(yhat[i]))+((1-y[i])*log2(1-(yhat[i]))) 
    
O=-O/n
print("yhat:",yhat,"y:",y) 
print("O=",O) 
