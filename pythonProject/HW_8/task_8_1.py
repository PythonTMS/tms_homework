def fact2(n):
    if n <= 0:
        return 1
    else:
        return n * fact2(n - 2)


for i in range(5):
    myNum = int(input('Введите число:\n'))
    print(f'Двойной факториал равен: {fact2(myNum)}')
