class pair:
    pairno = 0
    pairs = {}
    numbers = []
    def __init__(self, array):
        pair.numbers = array
    def check(self, target):
        n = len(pair.numbers)
        for i in range(n):
            for j in range(n):
                if pair.numbers[i] + pair.numbers[j] == target and i != j:
                    pair.pairno += 1
                    pair.pairs[pair.pairno] = [i, j]

array = input().split(' ')
array_n = []
for i in array:
    array_n.append(int(i))
target = int(input())

p = pair(array_n)
p.check(target)
print(p.pairs)