class py_solution:
def __init__(self, nums, target):
self.lookup = {}
c = 1
for i in range(len(nums)):
for j in range(len(nums)):
if nums[i] + nums[j] == target:
self.lookup[c] = [i, j]
c = c + 1
def show(self):
print(self.lookup)
list_ = [10,20,10,40,50,60,70]
target = 50
answer = py_solution(list_, target)
answer.show()
