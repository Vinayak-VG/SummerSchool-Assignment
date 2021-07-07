

# question 2 


class MyClass:
     
    def show(self,target,arr):
        n = len(arr)
        d ={}
        j = 1
        for i in range (0,n):
            for k in range (0,n):
                if (arr[i] + arr[k])== target:
                    d[j] = [i,k]
                    j+=1
        print(d)


arr = list(map(int,input().split()))
target = int(input())

c = MyClass()
c.show(target,arr)
