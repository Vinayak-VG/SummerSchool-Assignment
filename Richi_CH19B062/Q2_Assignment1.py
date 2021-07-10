class PairElements:
    def __init__(self,num,target):
        self.dictionary = {}
        l = 1
        for i in range(len(num)):
            for j in range(len(num)):
                if num[i] + num[j] == target:
                    self.dictionary[l] = [i,j]
                    l = l + 1

    def print(self):
        print(self.dictionary)

# Driver Code

target = int(input("Target = "))
num = list(map(int, input().split()))
dict = PairElements(num, target)
dict.print()





