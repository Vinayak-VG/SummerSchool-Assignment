#!/usr/bin/python3
class ALPHA:
    I = []
    size=0
    
    def __init__(A):
        I=[]
        print("Enter the size of the array\n")
        size=int(input())
        print("Enter the Array contents\n")
        for n in range(0,size):
            I.append(int(input()))
        print("\n")
        print("The array I = ",I)
        A.size = size
        A.I=I
        
    def operate(A):
        size=A.size
        buffer=[]
        I=A.I
        output ={1 : [0,0]} 
        target=int(input("Enter the target number\n"))
        counter=0
        for i in range(0,size):
            for j in range(0,size):
                S=I[i]+I[j]
                if(S==target):
                    counter+=1
                    output[counter]=[i,j]
        print(output)
        #return output
                    
        
    
    

                
            
B=ALPHA()       
B.operate()       
        





# B=ALPHA()
# show=B.operate()
# print(show)
