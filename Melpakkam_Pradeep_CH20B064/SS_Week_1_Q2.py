class Pair:
    def __init__(self, a, target):
        self.a = a
        self.target = target
    def check(a):
        counter = 0
        dict = {}
        for i in range(len(pair.a)):
            for j in range(len(pair.a)):
                if pair.a[i] + pair.a[j] == target:
                    dict.update({counter: (i, j)})
                    counter += 1
        print(dict)


target = int(input("Target: "))
a = list(map(int, input().split()))
pair = Pair(a, target)
pair.check()























