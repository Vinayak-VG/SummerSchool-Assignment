class MagicClass:
    def __init__(self, l):
        self.data = l

    def find_pairs(self, target):
        l = self.data
        dct = {}
        x = 1
        for i in range(len(l)):
            for j in range(len(l)):
                if(l[i] + l[j] == target):
                    dct[x] = [i, j]
                    x += 1
        print(dct)


# if(__name__ == "main"):
instance_one = MagicClass([10, 20, 10, 40, 50, 60, 70, 25])
instance_one.find_pairs(50)
