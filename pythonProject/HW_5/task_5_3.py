for i in range(200, 300):
    summ = 0
    for el in range(1, i):
        if i % el == 0:
            summ += el
    summ1 = 0
    for el1 in range(1, summ):
        if summ % el1 == 0:
            summ1 += el1
    if summ1 == i and summ != i:
        print(f'Числа {i} и {summ} - дружественные')
