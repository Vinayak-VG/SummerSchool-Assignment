from os import system
system('cls')
import numpy as np

class Storage:
     arr=[]
     lent=0
     target=0
     Final={}
     Key=1
     def __init__(self):
         Storage.declare_array()                 
         Storage.declare_target()

     def declare_array():                                     # Function to fetch array elements and target sum from user
        flag=1      
        x=''
        while(flag):                                               # flag to either continue fetching array elements or stop fetching
          x=input("Input array element(integer): ")
          (Storage.arr).append((int)(x))
          flag=(int)(input("Press a non zero digit if you wish to add more elements.Else press 0: "))
          Storage.lent=Storage.lent+1
          system("cls")
         
        print("Input array:\n",Storage.arr)
     def declare_target():                                   #Function to fetch target sum
         Storage.target=input("Input Target Sum:  ") 

     def find_target(self):                                  #Function to find indices of elements adding to target sum
         i=0
         while(i<Storage.lent):
             j=0
             
             while(j<Storage.lent):
                 a1=Storage.arr[i]+Storage.arr[j]
                 a2=Storage.target            
                 if((int)(a1)==(int)(a2)):
                     (Storage.Final)[f'{Storage.Key}']=[i,j]        #adding to dictionary if target sum is equal to sum of the pair of elements taken
                     Storage.Key=Storage.Key+1
                 j=j+1
             i=i+1

     def display_result(self):
         if(Storage.Final=={}):
             print("No pair of elements add to given target sum")
         else:   
             print(Storage.Final)        

c1=Storage()
c1.find_target()
c1.display_result()