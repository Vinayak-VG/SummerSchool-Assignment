class objec:
 arr=[]
 n=int(input("no of elements "))
 for i in range (0,n):
   ele=int(input("Enter the number "))
   arr.append(ele)
 target=int(input("enter the target "))
 sno={}

 count=0
 for k in arr:
    for m in arr:
        if k+m == target:
              count=count+1
              #print(k,m)
              sno[(count)]=[k,m]
              
     

ans=objec()
print(ans.sno)

