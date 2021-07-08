class myClass:
    # lst               # lst is the list containing the input numbers 
    # target            # target is the target number
    def show_pairs(self,lst,target):
        self.dictionary = {}       # Dictionary containing the solutions
        i = 0
        counter = 0
        while (i < len(lst)):
            j = 0
            while( j < len(lst) ):
                if(lst[i] + lst[j] == target):
                    counter = counter + 1
                    self.dictionary[counter] = [i,j]
                j = j + 1
            i = i + 1
        print("The dictionary containing the pairs is:",self.dictionary)

lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    print("Enter the",i+1,"th element: ",end = '')
    ele = int(input())
    lst.append(ele) # adding the element
     
print(lst)

target = int (input("Enter the target number: "))
print(target)

obj = myClass()
obj.show_pairs(lst,target)