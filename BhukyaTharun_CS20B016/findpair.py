#https://docs.python.org/3/tutorial/classes.html#:~:text=Python%20classes%20provide%20all%20the,class%20with%20the%20same%20name.

class Findpairs:
    dictionary={}
    count = 0
    def __init__(self,arr,target):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i]+arr[j] == target:
                    self.count += 1
                    self.dictionary[self.count]=[i,j]

arr=[10,20,10,40,50,60,70]
target=50
result=Findpairs(arr,target)
print(result.dictionary)