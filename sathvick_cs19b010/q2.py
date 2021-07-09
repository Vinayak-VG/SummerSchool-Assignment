
class Solver:
	def __init__(self):
		self.array = []
		self.target = 0

	def __init__(self, input_array, input_target):
		self.array = input_array
		self.target = input_target

	def solve(self):
		start, end = 0, len(self.array) - 1

		solution = [[i, j] for i in range(len(self.array)) for j in range(len(self.array)) if self.array[i] + self.array[j] == self.target]

		return dict(zip(range(1, len(solution) + 1), solution))


input_target = int(input())

input_str_array = input().split(' ')
input_array = [int(input_element) for input_element in input_str_array]

solver = Solver(input_array, input_target)

print(solver.solve())
