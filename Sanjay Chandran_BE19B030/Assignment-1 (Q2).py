class automated:
    def __init__(self,listy,target):
        self.listy = listy
        self.target = target
        self.dic = {}
        self.sno = 0
    def intel(self):
        for i in range(0,len(self.listy)):
            for j in range(0,len(self.listy)):
                if(self.listy[i]+self.listy[j] == self.target):
                    self.sno += 1
                    self.dic[self.sno] = [i,j]
        print(self.dic)

list_automated = automated([10,20,10,40,50,60,70],50)
list_automated.intel()
