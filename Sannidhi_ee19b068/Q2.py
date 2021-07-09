from numpy import * 
output=dict()
class pairofele: 
    def __init__(self,numbers,target): 
        self.numbers=numbers 
        self.target=target 
        count=1
        for i in range(len(numbers)): 
            for j in range(len(numbers)):                
                if numbers[i]+numbers[j]==target:                     
                    d={count:[i,j]}
                    count+=1
                    output.update(d)
#Test1=pairofele([10,20,10,40,50,60,70],50) 
#Test2=pairofele([14,15,25,36,17,18,22,21],39)
#Test3=pairofele([4,10,6,14,18,19,20],20)
print("Output:",output)

