class MyClass:
    def __init__(self,array,target):
      self.array=array
      self.target=target

    def function(self):
      n = len(self.array)
      ans_dict={}
      p=1
      for i in range(0,n):
          for j in range(0,n):
              if(self.array[i]+self.array[j] == self.target):
                  list=[i,j]
                  ans_dict[p]=list
                  p=p+1
      print(ans_dict)

array = list(map(int,input("Please Enter the numbers with space between them : ").split()))
target=int(input("Please Enter Target values : "))
object=MyClass(array,target)
object.function();
