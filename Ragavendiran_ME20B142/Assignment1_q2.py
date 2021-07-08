#declaring required variables
dict={}
lst=[]
ind=1

#input from user
n= int(input("Enter no of elements in list:  "))
print("Enter elements:")

for i in range(0,n):
    ele=int(input())
    lst.append(ele)

trg= int(input("Enter target sum:"))

#for checking
#print(lst)

#Finding indices

for q in range(0,n):
    for w in range(0,n):
        if lst[q]+lst[w]==trg:
            dict[ind]=[q,w]
            ind=ind+1

print(dict)

