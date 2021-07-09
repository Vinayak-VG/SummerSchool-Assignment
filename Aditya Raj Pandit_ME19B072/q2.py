def find_pair(a, t):
    output_dict = {}
    n = 1
    for i in range(len(a)):
        if (t - a[i]) in a:
            occur_list = occurs(t - a[i], a)
            for j in range(len(occur_list)):
                output_dict[n] = [i, occur_list[j]]
                n = n + 1
    return output_dict


occurs = lambda value, array: [i for i, e in enumerate(array) if value == e]


target = 20
input_number = [4, 10, 6, 14, 18, 19, 20]
output = find_pair(input_number, target)
print(output)
if 5>2:
    print("je")
else if 5<2:

