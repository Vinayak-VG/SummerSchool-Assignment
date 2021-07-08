numbers = [10, 20, 30, 40, 50]
target = 50

class pair_finder:
    
    # numbers = [10, 20, 30, 40, 50]
    # target = 50
    
    def __init__(self, numbers, target):        
        self.numbers = numbers
        self.target = target
        
    def show(self):
        print("The numbers in the array are", self.numbers)
        print("The target sum is", self.target)

    def find_pairs(self):
        
        ind = {}
        ans = {}
        cou = 0
        
        for i in range(0, len(self.numbers)):
            for j in range(0, len(self.numbers)):
                
                # Avoiding the same element:                
                if(i == j):
                    continue
                
                if(self.numbers[i] + self.numbers[j] == self.target):
                    ind[cou + 1] = [i, j]
                    ans[cou + 1] = [self.numbers[i], self.numbers[j]]
                    cou = cou + 1
        
        print("Numbers in the array =", self.numbers)
        print("Target sum =", self.target)
        print("Number of pairs found =", cou)
        print("Dictionary of all the pairs (Indexes) =", ind)
        print("Dictionary of all the pairs (Values) =", ans)
        
        if(cou != 0):
            print("\nNote: Each pair is intentionally repeated (Order is changed).")
            print("This is true even if the 2 numbers are the same.")
            print("A minor modification in the code can remove this feature if it is not required.")
    
pf = pair_finder(numbers, target)

# pf.show()

pf.find_pairs()
