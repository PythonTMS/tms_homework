myStr = input('Введите строку:\n')
myList = myStr.split(' ')
myList1 = []
for i in range(len(myList)):
    myList1.append(myList[-i - 1])
print(' '.join(myList1))
