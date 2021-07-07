

# question 2 

arr = list(map(int,input().split()))
target = int(input())
n = len(arr)
d ={}
j = 0
for i in range (0,n-1):
    for k in range (0,n):
        if (arr[i] + arr[k])== target:
            d[j] = [i,k]
            j+=1

print(d)
