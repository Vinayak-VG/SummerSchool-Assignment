
array = [10,20,10,40,50,60,70]
target = 50
n=len(array)


class Pairing:
    
    def __init__(self,array,target):
        output = {}
        self.output = output
        r=0
        i=0
        while i<n:
            k=0
            while k+i < n:
                if array[i]+array[k] == target:
                    ans= [i,k]
                    output[r]=ans
                    r=r+1
                    
                k=k+1
                
            i=i+1
        

    def show(self):
        print(self.output)

solution= Pairing(array, target)
solution.show()


