# problem 2

class elements():

    def find_values(self,n,target):

        x = 1

        Out = {}

        for i in range(6):
            for j in range(6):
                if ele[i] + ele[j] == tar:
                    Out[x] = [i, j]
                    x = x + 1

        print(Out)


a=elements()
ele=[4,8,0,11,12,15]
tar=12
a.find_values(ele,tar)
