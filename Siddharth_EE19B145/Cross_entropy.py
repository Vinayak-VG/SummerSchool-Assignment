import numpy as np

#Question 1: Compute the cross entropy using randomly generated arrays;

#The size of the arrays:
n=100;

#The 2 arrays:
y=np.random.randint(2,size=n);  #Array with only 0s and 1s
y_cap=np.random.rand(n);  #Array with values in the interval [0,1)

#The cross entropy:
O=-sum(y*np.log2(y_cap)+(1-y)*np.log2(1-y_cap));
O/=n;
print("Question 1: ")
print("The cross entropy is :"+str(O),'\n');
