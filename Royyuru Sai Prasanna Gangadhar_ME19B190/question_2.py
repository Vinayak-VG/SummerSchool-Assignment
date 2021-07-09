class myclass:
    k= 1
    ls = []
    my_dict = {}
    def return_index(self,target):
        for i in range(len(self.ls)):
            for j in range(len(self.ls)):
                if (self.ls[i] +  self.ls[j]) == target :
                    self.my_dict[self.k] = [i,j]
                    self.k = self.k +1
                else:
                    continue

if __name__ == "__main__":
    x= myclass()
    s = int(input('Target Value:'))
    while (True):
        y = input("Enter only integer values and press 'e' to escape:")
        if y == 'e' :
            break
        else:
            x.ls.append(int(y))
    print('Your input', x.ls)
    x.return_index(s)
    print('Output is:',x.my_dict)