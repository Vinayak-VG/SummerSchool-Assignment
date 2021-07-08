class Pair_Sum:
	def __init__(self,array,sum_goal):
		self.array = array;
		self.sum_goal = sum_goal;
		self.dict = {}
	def compute_dict(self):
		count = 1;
		for i in range(len(self.array)):
			for j in range(len(self.array)):
				if(self.array[i]+self.array[j]==self.sum_goal):
					self.dict[count] = [i,j]
					count+=1
sum_goal = int(input())
array = [int(a) for a in input().split()]
solver = Pair_Sum(array,sum_goal)
solver.compute_dict()
print(solver.dict)
