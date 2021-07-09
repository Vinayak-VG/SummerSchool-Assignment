"""
Python and GIT Basics Assignment
Question-2 Solution

By: P Akhil Reddy
Roll No: CH20B076
Contact: 8074147570
Email: ch20b076@smail.iitm.ac.in

Problem Statement: Write a Python class to find a pair of elements(indices of the two numbers) from a given array which whose sum equals a target number

Sample input:
10 20 10 40 50 60 70
50

Output:
{1: [0, 3], 2: [2, 3], 3: [3, 0], 4: [3, 2]}

"""

class MyClass:
  pairs = {}
  #we declare a dictionary which will contain the required pairs from the list

  def func(self, list1, target):

    #passing these values as MyClass attributes
    self.target = target
    self.list1 = list1

    num1 = 1
    #here we use num1 for setting keys to the dictionary

    #we will take two variables which iterate through the list and find out if any pair adds up to the target number
    for i in range(len(list1)):
      for j in range(len(list1)):

        if ((self.target == self.list1[i] + self.list1[j]) and i  != j):
          self.pairs.update( {num1: [i, j]} )
          # appending a new satisfying pair to the dictionary

          num1 += 1
          # incrementing num1 to set key for next pair

    print(self.pairs)
    #outputs the dictionary containing the required pairs

    #if we find no such pairs from the list then the below code will be executed 
    if (num1 == 1 and self.pairs == {}):
      print("The target cannot be obtained by adding any pair of numbers from the list")

#taking inputs for list1 and the target number
list1 = list(map(int, input().split()))
num = int(input())

#creating an object obj and using that object method to compute and output the required pairs
obj = MyClass()
obj.func(list1, num)