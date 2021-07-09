class TargetElements:
    
    def __init__(self, target, array):
        self.dict = {}
        self.target = target
        self.array = array
        
    def find(self):
        count = 0
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if self.array[i] + self.array[j] == self.target:
                    self.dict[count] = [i, j]
                    count = count + 1
                    
        print(self.dict)

array = [int(x) for x in input().split(',')]
target = int(input())
Answer = TargetElements(target, array)
Answer.find()


