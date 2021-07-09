class Task2:
    def solve(self, array, target):
        count = 1
        answer = {}
        for i in range(len(array)):
            for j in range(len(array)):
                if i != j and array[i] + array[j] == target:
                    answer[count] = [i, j]
                    count += 1
        for key in answer:
            print(key, ":", answer[key])


array = [10, 20, 10, 40, 50, 60, 70]
test = Task2()
test.solve(array, 50)