class Pair:
    def __init__(self, numbers, target):
        self.num = numbers
        self.target = target
        self.ans = {}
        
        c = 0
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if (self.nums[i] + self.nums[j] == self.target):
                    c += 1
                    self.ans[c] = [i, j]

    def display(self):
        print(self.ans)
