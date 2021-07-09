class Pairs:
    def __init__(self,numbers,target):
        k = 1
        out = {}
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i]+numbers[j] == target:
                    out[k] = [i,j]
                    k = k+1
        self.out = out
        print("Output: ",out)
        return 0
