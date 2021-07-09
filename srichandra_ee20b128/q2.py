class target_sum:
    def __init__(self,numbers,target):
        k=0
        self.lookup = {}    #creating dictionary

        #looping for finding the pairs
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    self.lookup[k] = [i,j] #adding the key and value to dictionary
                    k = k+1
    
    # method for displaying the dictionary
    def show(self):
        print(self.lookup)

# given list and target (objects)
list = [10,20,10,40,50,60,70]
target = 50

# displaying the result
answer = target_sum(list, target)
answer.show()