import numpy as np

class sumTarget:
	def output(self, data, target):
		count = 0
		ansDict = {}

		for i in range(len(data)):
			for j in range(len(data)):
				if data[i] + data[j] == target:
					count += 1
					ansDict[count] = [i, j]
		return ansDict

print(' INPUT CONVENTION: Say the array has 6 \'integers\',')
print(' then simply enter the numbers with a space in between.')
print(' EXAMPLE: 30 90 10 20 20 40')

data = list(map(int, input('\n Enter an array of numbers: ').split()))
target = int(input(' Enter the target: '))

print(' Output for target sum pairs: ', sumTarget().output(data, target))