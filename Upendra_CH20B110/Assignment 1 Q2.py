class Example:
  target = 'dummy' # Dummy initialisation
  numlist = []
  pairs = {}
  def __init__(self):
    print("Number of elements in list: ")
    n = int(input())
    print("Input the values")
    for i in range(0,n,1):
      self.numlist.append(int(input()))
    print("Enter target : ")  
    self.target = int(input())  
  def genindexpairs(self):  # method to find the pairs of indices
    self.pairs = {}
    ctr = 0
    for i in range(len(self.numlist)):
      for j in range(len(self.numlist)):
        if self.numlist[i] + self.numlist[j] == self.target:
          self.pairs[ctr+1] = [i,j]
          ctr = ctr + 1
  def DispAll(self):
    print("List : ",self.numlist)
    print("Target : ",self.target)
    print("Index Pairs : ", self.pairs)
  def DispPairs(self):
    print(self.pairs)  
obj = Example()
obj.genindexpairs()
obj.DispPairs()