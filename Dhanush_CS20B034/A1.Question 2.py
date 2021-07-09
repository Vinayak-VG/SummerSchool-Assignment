class Finder:
	def __init__(self,numlist,target):
		self.numlist = numlist
		self.target = target
		self.find()
	
	def find(self):
		self.ans = dict([])
		self.indexdict = 1
		for x in range(len(self.numlist)):
			k=x+1
			for y in range (k,len(self.numlist)):
				if((self.numlist[x] + self.numlist[y])==self.target):
					self.ans[self.indexdict]= [x,y]
					self.indexdict = self.indexdict+1
	
	def show(self):
		print(self.ans)
		
numlist = [10,20,30,40,50,60,70,80]
target = 50

answer = Finder(numlist,target)
answer.show()