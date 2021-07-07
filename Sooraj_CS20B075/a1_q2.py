class PairFind:
	def __init__(self, array, target):
		self.array = array
		self.target = target
		self.findpair()
	def findpair(self):
		self.ans = dict([])
		self.size = len(self.array)
		self.index = 1
		for x in range(self.size):
			for y in range(self.size):
				if self.array[x] + self.array[y] == target:
					self.ans[self.index] = [x, y]
					self.index += 1

	def show(self):
		print(self.ans)

array = [10,20,10,40,50,60,70]
target = 50

a = PairFind(array, target)
a.show()

