myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = []
for el in myList:
    newList.append(el * -2)
print(myList)
print(newList)

print('-----------------------------------')

myList2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
newList2 = []
i = 0
while i < len(myList2):
    newList2.append(myList2[i] * -2)
    i += 1
print(myList2)
print(newList2)
