import numpy as np

class xyz:
    def __init__(self, arr, Tsum):
        self.arr = np.array(arr)
        self.Tsum = Tsum
    def dik(self):
        dik = {}
        k = 0
        values = []
        tmp = self.arr
        for _ in range(len(self.arr)):
            tmp = self.arr[_] + self.arr
            res = np.where(tmp == self.Tsum)
            if len(res[0]) != 0:
                for i in range(len(res[0])):
                    if _ != res[0][i]:
                        k += 1
                        dik[k] = [_, res[0][i]]
        print(dik)
            

        
arr = list(map(int, input().split()))
Tsum = int(input())
p = xyz(arr, Tsum)
p.dik()