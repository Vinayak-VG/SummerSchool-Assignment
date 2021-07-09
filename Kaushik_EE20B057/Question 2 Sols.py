class Finder:
    def List(Input, Target, Length):
        Index = 1
        Output = {}
        for i in range(0,Length):
            for j in range(0,Length):
                Check = Input [i] + Input[j] 
                if (Check == Target):
                    Output[Index] = [i, j]
                    Index = Index + 1
        return Output
    
    
    Input = [14, 15, 25, 36, 17, 18, 22, 21]
    Target = 39
    Length = len(Input)
    
    Output = List(Input, Target, Length)
    
    
    

Test = Finder()
Arr1 = Test.Input
Tar = Test.Target
L = len(Arr1)
print(Arr1)
print(Tar)
OutList = Test.Output
print(OutList)
   
            