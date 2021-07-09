class FindPairs:
    dict = {}
    count = 0

    def __init__(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    self.count += 1
                    self.dict[self.count] = [i, j]

arr = [10, 20, 10, 40, 50, 60, 70]
target = 50
example = FindPairs(arr, target)
print(example.dict)
