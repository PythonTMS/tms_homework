while True:
    x = int(input('Введите число x:\n'))
    y = int(input('Введите число y:\n'))
    sign = input('Введите знак операции(+, -, /, *):\n')
    if sign == '+':
        z = x + y
        print(z)
    elif sign == '-':
        z = x - y
        print(z)
    elif sign == '/':
        if y == 0:
            print('В этой вселенной на 0 делить нельзя')
            continue
        z = x / y
        print(z)
    elif sign == '*':
        z = x * y
        print(z)
    elif sign == '0':
        print('И тут внезапно калькулятор перестает работать')
        break
    else:
        print('Неверно введен знак операции')
