import numpy as np

class Find:
    
    def __init__(self, array, target) -> None:
        self.array = array
        self.target = target
    def find_output(self) -> dict:
        diff_array = self.target - self.array
        dict = {}
        i=1
        for y in range(len(self.array)):
            
            found = np.where(diff_array == self.array[y])
            
            if (len(found[0]) > 0):
                for x in found[0]:
                    dict[i] = [y, x]
                    i = i+1
        return dict

numbers = np.array([10, 20, 10, 40, 50, 60, 70])
target = 50

print(Find(numbers, target).find_output())










