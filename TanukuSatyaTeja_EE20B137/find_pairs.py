
t_sum = int(input("Please enter target sum: "))

num = [int(number) for number in input("Enter the numbers to be checked (seperated by space) : ").split()]

class find_pairs :

    pairs = {}

    def __init__(self,array,sum):
        n = len(array)
        k = 1
        
        for i in range (0, n):
            for j in range (0,n):
                if(array[i] + array[j] == sum):
                    self.pairs[k] = [i, j]
                    k +=1

        self.numbers = array
        self.target_sum = sum

    def show(self):
        print (self.pairs)


pair = find_pairs(num,t_sum)

pair.show()




