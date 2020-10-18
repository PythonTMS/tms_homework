myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for el in myList:
    if el % 2 == 0:
        count += 1
print(f'Кол-во четных чисел: {count}')

print('--------------------------------------------')

myList2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 0
count2 = 0
while i < len(myList2):
    if myList2[i] % 2 == 0:
        count2 += 1
    i += 1
print(f'Кол-во четных чисел: {count2}')
