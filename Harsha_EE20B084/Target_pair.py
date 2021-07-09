n = int(input("Enter number of elements : "))

numbers = []
for i in range(n):
    numbers.append(int(input()))
    
target = int(input("Enter target : "))

class pair:
    
    k = 0

    def show(self,arr,trgt,r):
        S_No = {}
        for i in range(r):
            for j in range(r):
                
                if(i!=j and arr[i] + arr[j] == trgt) :
                    self.k = self.k+1
                    S_No[self.k] = [i,j]
        return(S_No)
                    
S_No = pair().show(numbers,target,n)

print(S_No)