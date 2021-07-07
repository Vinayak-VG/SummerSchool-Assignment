# class that has a function find_tar to find the target
class get_values(object):
   def find_tar(self, data, target):      
       #dictionary to store the indicies
       final_dict = {}
       i = 0
       j = 0
       count = 0
       #double for loop to find the indices. both loop starts from 0 , because in question, they expect both [0,4], [4,0] in output 
       for i in range(len(data)):
          for j in range(len(data)):
             if data[i] + data[j] == target :
                count=count+1
                final_dict.update({count : (i, j)})
                
        #if no two indices is found to get target        
       if count==0:
           return "none"
       
       else:
           return final_dict
 #checking the user's opinion of already given array or user's choice      
check = input("press 1 to show result for already inputed data orelse press 2 to input new array of integers : \n ")
check = int(check)
if (check == 1) :
    tr = [10,20,10,30,40,50,60,70]            
    print("for already inputed data " ,tr,"-->", get_values().find_tar(tr,50))

else : 
    tr1 = []
    tr1 = [int(num) for num in input("Enter the list of integers seperated by a space : \n").split()]
    tar = input("enter the target ie. the no. which can be obtained by adding any two no. from the array u entered: \n")
    tar = int(tar)
    print(tr1,"-->", get_values().find_tar(tr1,tar))
  