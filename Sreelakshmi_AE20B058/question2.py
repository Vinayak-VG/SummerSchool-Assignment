class sum_checker:
    def __init__(self,numbers,target):
        self.numbers=numbers
        self.target=target

    def checker(self):
        count=1
        dict={1:[-1,-1]}
        for index1 in range(len(self.numbers)):
            for index2 in range(len(self.numbers)):
                if(self.numbers[index1]+self.numbers[index2]==self.target):
                    dict[count]=[index1,index2]
                    count=count+1
        print (dict)
        


input_numbers=[]
input_numbers=[int(number) for number in input().split()]
input_target=int(input())
#assuming that input is entered as:
#<numbers[0]> <numbers[2]> ...... <numbers[n]>
#<target>

obj=sum_checker(input_numbers,input_target)
obj.checker()


