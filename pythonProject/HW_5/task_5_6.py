import random
myArr = [random.choice([i for i in range(30)]) for j in range(20)]
print(myArr)
count = 0
for i in range(1, len(myArr) - 1):
    if myArr[i] >= myArr[i - 1] and myArr[i] > myArr[i + 1]:
        count += 1
print(count)
