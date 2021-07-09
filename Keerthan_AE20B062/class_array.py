class find_element():
    def __init__(self):
        self.dict = {}
        self.count = 1

    def find(self, numbers, target):
        for x in range(len(numbers)-1):
            for y in range(x+1, len(numbers)):
                if numbers[x] + numbers[y] == target:
                    self.dict[self.count] = [x, y]
                    self.count += 1
a = find_element()
a.find([10, 20, 10, 40, 50, 60, 70], 50)
print(a.dict)
