# problem 2

class pair_of_elements():

    def find_values(self,n,target):

        x = 1

        Out = {}

        for i in range(6):
            for j in range(6):
                if n[i] + n[j] == target:
                    Out[x] = [i, j]
                    x = x + 1

        print(Out)


ll=pair_of_elements()
n=[4,8,0,11,12,15]
target=12
ll.find_values(n,target)
