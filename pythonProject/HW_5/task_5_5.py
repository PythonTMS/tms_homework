import random
myArr = [random.choice([i for i in range(30)]) for j in range(19)]
print(f'Массив:\n{myArr}')
greater = 0
for i in range(len(myArr)):
    if greater < myArr[i]:
        greater = myArr[i]
for i in range(len(myArr)):
    if myArr[i] % 2 == 0:
        myArr[i] = greater
print(f'Наибольший элемент массива:\n{greater}')
print(f'Измененный массив:\n{myArr}')
