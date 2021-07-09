class target_sum:
    dictionary = {}

    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    
    def crt_dict(self):
        count=0
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):
                if self.arr[i]+self.arr[j]==self.target:
                    count+=1
                    self.dictionary[count]=list([i,j])
        print(self.dictionary)

tar=int(input('enter target sum'))
num=int(input('enter the total number of input numbers'))

arr=[]
for i in range(num):
    arr.append(int(input()))

obj= target_sum(arr,tar)
obj.crt_dict()
