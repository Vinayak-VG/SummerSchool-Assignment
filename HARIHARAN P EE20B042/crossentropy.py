import numpy as np

#getting log2 function from library
from math import log2 
 
#Y = y cap vector and y = y vector
 
#calculating cross-entropy loss 
def cr_en (Y, y):
  return -0.01 * (sum ([y[i] * log2 (Y[i]) + (1 - y[i]) * log2 (1 - Y[i]) for i in range (len (y))]))
  


#initialising values
  
import random 
y =[] 
for i in range (0, 100):
    n = np.random.randint (0, 1) 
    y.append (n) 
 
import random 
Y =[] 
for i in range (0, 100):
    m = np.random.random () 
    Y.append (m) 
 
#calculate cross-entropy loss O(Y,y)
O = cr_en (Y, y) 
print ('O(Y, y):  %.6f ' % O) 
