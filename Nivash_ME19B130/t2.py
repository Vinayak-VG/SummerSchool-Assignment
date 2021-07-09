class Sumdict:
	def __init__(self,arr,tar):
		self.arr=arr
		self.tar=tar
		self.dictn={}
	def display(self):
		k=0
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				if ((self.arr[i]+self.arr[j])==self.tar):
					k=k+1
					self.dictn[k]=[i,j]
		print(self.dictn)
s=Sumdict([10,20,10,40,50,60,70],50)
s.display()
