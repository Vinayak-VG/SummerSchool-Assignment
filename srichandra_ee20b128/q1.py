import numpy as np    # importing numpy library

y = np.random.rand(1,100) #creating a numpy array with random numbers in range [0,1)
y1 = np.random.randint(0,2,(1,100)) # creating a numpy array with random 0's or 1's

O = y1*np.log2(y) + (1-y1)*np.log2(1-y) #finding the required 'O' array
#print(O)

cross_entropy = -1*np.sum(O)/100.0 # finding the cross-entropy
print(cross_entropy)