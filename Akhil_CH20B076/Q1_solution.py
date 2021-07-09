"""
Python and GIT Basics Assignment
Question-1 Solution
By: P Akhil Reddy
Roll No: CH20B076
Contact: 8074147570
Email: ch20b076@smail.iitm.ac.in

Problem Statement: Compute the cross entropy loss O for two vectors of same dimensions

Here we will specify the vectors and their dimensions through input

Sample input:
5
0.32 0.56 0.71 0.14 0.57
1 0 1 1 0

Output:
1.475297

"""

import numpy as np
import math as m

#we will define a function which computes the cross entropy loss with the given vectors
def cross_entropy_loss(n, y, y_hat):
  O = 0
  for i in range(n):
    O += (-1/n)*((y[i] * m.log2(y_hat[i])) + ((1-y[i]) * m.log2(1-y_hat[i])))
  return O

n = int(input())
#taking input for size of numpy vector

O = 0
#initialising the variable which will store the value computed by cross-entropy loss function

list1 = list(map(float, input().split()))
#taking input for the first vector

list2 = list(map(int, input().split()))
#taking input for the second vector

y = np.array(list2)
#initialising the first vector y using numpy

y_hat = np.array(list1)
#initialising the second vector y_hat using numpy

#we will now compute the cross entropy loss using the defined function and round off to 6 digits after decimal
O = round(cross_entropy_loss(n, y, y_hat), 6)

print(O)
#outputs the computed value O