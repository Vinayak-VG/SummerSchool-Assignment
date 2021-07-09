def search(N, target):
    solutions={}
    ct=0
    for i in range(len(N)):
        for j in range(len(N)):
            if N[i] + N[j] == target:
               ct=ct+1
               solutions[ct]=[i,j]
    print(solutions)
N = [4, 10, 6, 14, 18, 19, 20]
target = 20
search(N, target)
