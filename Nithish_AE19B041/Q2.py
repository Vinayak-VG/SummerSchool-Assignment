class index_finder:
	def __init__(self,numbers,target):
		self.numbers=numbers
		self.target=target
	def finder(self):
		k=0
		dic={}
		for i in range(len(self.numbers)):
			for j in range(len(self.numbers)):
				if i!=j:
					if self.numbers[i]+self.numbers[j]==self.target:
						dic[k+1]=[i,j]
						k+=1
		if k==0:
			print("No two element sum is equal to target")
		else:
			print(dic)

c=index_finder([10,20,10,40,50,60,70],50)
c.finder()		
