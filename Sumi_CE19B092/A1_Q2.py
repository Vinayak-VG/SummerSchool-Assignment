class array:
    def FindTarget(self, numbers, target):
        result = {}
        index = 1
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    result[index] = [i, j]
                    index = index + 1
        return result

numbers = list(map(int, input().split()))
target = int(input())
pairs = array()
print(pairs.FindTarget(numbers, target))
