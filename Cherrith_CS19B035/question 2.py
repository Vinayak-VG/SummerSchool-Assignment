import numpy as np

class Target:
    def __init__(self,array,target):
        self.array = array
        self.target = target

    def get_pairs(self):
        array_size = np.size(self.array,0)

        answer_dict = {}
        index = 1

        for i in range(0,array_size):
            for j in range(0,array_size):
                if(int(self.array[i]) + int(self.array[j]) == self.target):
                    list = [i,j]
                    answer_dict[index] = list
                    index += 1

        print(answer_dict)

# test code

array = np.array(input("Array : ").split())
target = int(input("Target : "))
solve = Target(array,target)
solve.get_pairs()