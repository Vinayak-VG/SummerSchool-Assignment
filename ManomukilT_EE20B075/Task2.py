class index: #class to store the indices

    def __init__(self,index1,index2): #member function to store the index values

        self.index1 = index1
        self.index2 = index2

    def publist(self): #member function that returns the index values in the form of a list

        retlist = list()
        retlist.append(self.index1)
        retlist.append(self.index2)

        return retlist

    
if __name__ == '__main__':

    strinput = input("Enter the array : ")
    number = int(input("Enter the number : "))
    temp = strinput[1:len(strinput)-1] #to remove the square brackets
    try:
            
        numlist = [int(x) for x in temp.split(', ')]

    except:

        print("Invalid Input")
        exit


    serialnum = 0
    findict = dict()

    for i in range(len(numlist)):

        for j in range(len(numlist)):

            if numlist[i]+numlist[j] == number:

                indices = index(i,j)

                indexstr = indices.publist()

                serialnum = serialnum + 1

                findict[serialnum] = indexstr

print(findict)




            

