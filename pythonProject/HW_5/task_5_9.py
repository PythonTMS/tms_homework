m = int(input('Введите число m:\n'))
n = int(input('Введите число n:\n'))
for i in range(m, n + 1):
    myList = []
    for j in range(2, i):
        if i % j == 0:
            myList.append(str(j))
    print(f"{i}:{', '.join(myList)}")
