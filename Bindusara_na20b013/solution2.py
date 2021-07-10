import numpy

class elements:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    def dict(self):
        dictionary={}
        key_index=1
        length=len(self.arr)
        for i in range(0,length):
            for j in range(0,length):
                if (self.arr[i]+self.arr[j])==self.target:
                    dictionary[key_index]=[i,j]
                    key_index=key_index+1
        print(dictionary)

p=elements([14, 15, 25, 36, 17, 18, 22, 21],39)
p.dict()
