class pairs:
    def __init__(self,arr):
        self.data = arr
    def getpair(self,tar):
        arr = self.data
        keys = 1
        dict = {}
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(arr[i] + arr[j] == tar):
                    dict[keys] = [i,j]
                    keys+= 1
        return(dict)

arr = pairs([10,20,10,40,50,60,70,25])
print(arr.getpair(50))