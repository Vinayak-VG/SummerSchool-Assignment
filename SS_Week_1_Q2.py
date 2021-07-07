def check(a):
    counter = 0
    dict = {}
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] + a[j] == target:
                dict.update({counter: (i, j)})
                counter += 1
    print(dict)


target = int(input("Target: "))
a = list(map(int, input().split()))
check(a)











