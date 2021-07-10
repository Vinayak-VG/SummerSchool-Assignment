n = int(input("Enter number of elements : "))
n = int(n)
print(n)
print("Enter elements : ")
arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)
target = int(input("Enter target number : "))
print(target)
d = dict()
counter = 1
for i in range(n):
    for j in range(n):
        if(arr[i] + arr[j] == target):
            d[counter] = [i,j]
            counter+=1
print(d) 