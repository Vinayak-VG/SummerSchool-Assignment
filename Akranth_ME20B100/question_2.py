class elements_pair:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    def add88(self,i,j):
        return self.arr[i]+self.arr[j]
    
    def show_dict(self):
        print(len(self.arr))
        dictinary={}
        a=1
        for i in range(0,len(self.arr)):
            for j in range(0,len(self.arr)):
                if i!=j and self.add88(i,j)==self.target :
                    dictinary[a]=[i,j]
                    a=a+1
        print(dictinary)



#Give input as a array of number and target number.
q=elements_pair([14,15,25,36,17,18,22,21],39)
#show_dict() method give the required answer.
q.show_dict()

