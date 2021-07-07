class myDict:
    def _init_(self,arr,tar):
        self.array=arr
        self.target=tar

    def show(self):
        n=len(self.array)
        mydict={}
        resdict={}
        k=1
        for i in range(n):
            mydict[(self.array)[i]]=[]
        for i in range(n):
            mydict[(self.array)[i]].append(i)

        for num in mydict:
            if self.target-num in mydict:
                for i in range(len(mydict[num])):
                    for y in mydict[self.target-num]:
                        resdict[k]=[mydict[num][i],y]
                        k+=1
        print(resdict)


print("enter a list of numbers: ")
arr=list(map(int,input().split()))
tar=int(input("enter the target number: "))
dict=myDict(arr,tar)
dict.show(
