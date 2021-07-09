class finder
  dict={}
  count=1
  
  def checktarget(self,m,tar,arr)
    for i in range (0,m)
      for j in range (0,m)
        if arr(i)+arr(j)==tar
          dict.update({count:[i j]})
          count++
    
arr=[]
obj=finder()            
n=int(input("Enter number of elements\n"))
for i in range (0,n)
  x=int(input())
  arr.append(x)
target=int(input("Enter target number")
obj.checktarget(n,target,arr)
print("Dictionary:\n",obj.dict)

