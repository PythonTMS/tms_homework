chislo = list(input('Введите число:\n'))
summa = 0
multi = 1
for el in chislo:
    summa += int(el)
    multi *= int(el)
print(f'Сумма цифр: {summa}')
print(f'произведение цифр: {multi}')
