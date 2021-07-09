#Question2: find_sum is the python class for finind dictionary of indices whose sum is equal to target

class find_sum:

    def __init__(self, a,target):
        self.a=a
        self.target=target
        

    def pair_dict(self):
        b={}
        sno=1
        for j,valj in enumerate(self.a):
             for i,vali in enumerate(self.a) :
                if vali + valj == self.target :
                    b[sno]=[j,i]
                    sno+=1
        return b


a = [int(i) for i in input("Enter array : ").split()]  # Input list

target=int(input("Enter target: "))                    # Input target

obj= find_sum(a,target)                                # Calling an instance of class find_sum

b= obj.pair_dict()                                     


print(b)
