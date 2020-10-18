myStr = input("Введите строку:\n")
centr = int(len(myStr) / 2)
print(f'Буква в середине: {myStr[centr]}')
if myStr[centr] == myStr[0]:
    print(myStr[:-1])
