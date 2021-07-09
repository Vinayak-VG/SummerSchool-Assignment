#creating array.
arr = []

print("Size of array")
m = int(input())

print("Enter the elements")
for i in range(m):
  element = int(input())
  arr.append(element)

#inputing the target
print("Target")
Target = int(input())

#creating class
class MyClass:
    def __init__(self,Arr,sum):
        self.Arr = Arr
        self.sum = sum

    def final(self):
        output = {}
        index = 1

        for i in range(len(self.Arr)):
            for j in range(len(self.Arr)):

                if(self.Arr[i]+self.Arr[j] == self.sum and i!=j):
                    output[index] = list([i,j])
                    index += 1
        return output

#creating instance of the class
result = MyClass(arr, Target)
result.final()

#output of program
print("Output")
print(result.final())