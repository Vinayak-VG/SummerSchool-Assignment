def logic(dic):
    prev ={}
    tkeys = list(dic.keys())
    while prev != dic:
        prev = dic.copy()
        for key in tkeys:
            tmp = dic[key]
            for item in tmp:
                if item not in tkeys:
                    dic.pop(key)
                    tkeys.remove(key)
                    break
    for v in dic.values():
        for i in v:
            if i not in tkeys:    
                tkeys.append(v)
    return(tkeys)         

# driver       
z, n, m = map(int, input().split())
states = []
for i in range(z):
    l = input().split()
    states.append(l)
dik = {}
#output
out = {}
for _ in range(z):
    out[states[_][0]] = states[_][n + 1:n + m + 1]
    
for _ in range(z - 1):
    for l in range(_ + 1, z):  
        values = []
        if out[states[_][0]] == out[states[l][0]]:
            for i in range(1, n + 1):
                if states[_][i] > states[l][i]:
                    values.append((states[l][i], states[_][i]))
                elif states[_][i] < states[l][i]:
                    values.append((states[_][i], states[l][i]))
            dik[(states[_][0], states[l][0])] = values
print(logic(dik))
