
t_sum = int(input("Please enter target sum: "))

num = [int(number) for number in input("Enter the numbers to be checked (seperated by space) : ").split()]

n = len(num)
k = 1
pairs = {}

for i in range (0, n):
    for j in range (0,n):
        if(num[i] + num[j] == t_sum):
            pairs[k] = [i, j]
            k +=1


print (pairs)