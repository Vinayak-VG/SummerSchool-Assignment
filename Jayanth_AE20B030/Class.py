class Target_Sum_Pair:
    dict_values = {}
    count = 1

    def dict_append(self, a, b):
        self.dict_values[self.count] = [a, b]
        self.count += 1

    def check_sum(self, arr, m, tar):
        for j in range(m):
            for k in range(m):
                if arr[j] + arr[k] == tar:
                    self.dict_append(j, k)


elements = []
obj = Target_Sum_Pair()
n = int(input("Enter the number of elements to be appended:"))
print("Enter the elements: ")
for i in range(n):
    elements.append(int(input()))

target = int(input("Enter the target number: "))
obj.check_sum(elements, n, target)
print("The Dictionary of pair of indices whose corresponding values sum to target is :", obj.dict_values)
