class Numbers:

    def __init__(self, listt, target):
        self.listt = listt
        self.target = target

    def process(self):
        l = {}  # empty dictionary
        count = 0
        size = len(self.listt)  # length of input list
        for i in range(size):
            for j in range(size):
                if self.listt[i] + self.listt[j] == self.target:
                    count += 1
                    l[count] = [i, j]

        return l


print("Enter the list of numbers: ", end=" ")
input_numbers = list(map(int, input().split()))
target = int(input("Enter the target number: "))
obj = Numbers(input_numbers, target)
print(obj.process())
