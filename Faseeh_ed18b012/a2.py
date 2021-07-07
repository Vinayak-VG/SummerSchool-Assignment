class FindPairs:
    def __init__(self,target, numbers):
        self.dict = {}
        self.target = target
        self.numbers = numbers

    def find_idx(self):
        count=0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if(self.numbers[j] == self.target - self.numbers[i]):
                    self.dict[count] = [i, j]
                    count += 1
        print(self.dict)

numbers = [int(x) for x in input().split(',')]
target = int(input())
F1 = FindPairs(target, numbers)
F1.find_idx()
