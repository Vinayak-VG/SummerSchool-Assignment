from os import system
system("cls")

import numpy as np

print("No of dimensions of the vector:  ")   #size of the vector(array)
x=input()
N=(int)(x)
system("cls")

y_hat=np.random.rand(1,N)                    #The two vectors 
y=np.random.randint(0,2,(1,N))

O=0                                          #Cross-entropy loss
i=0     

while(i<N):
    O=O-(1/N)*(  y[0][i]*np.log2(y_hat[0][i])  +   (1-y[0][i])*np.log2(1-y_hat[0][i])   )
    i=i+1

print("Cross-Entropy loss for the model=",O)    
