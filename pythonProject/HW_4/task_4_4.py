myList = [1, 2, 3, 4, 5, 6, 7]
temp = myList[0]
for i in range(len(myList) - 1):
    myList[i] = myList[i + 1]
myList[-1] = temp
print(myList)

print('--------------------------------------')

myList2 = [2, 3, 4, 5, 6, 7]
temp1 = myList2[0]
i = 0
while i < len(myList2) - 1:
    myList2[i] = myList2[i + 1]
    i += 1
myList2[-1] = temp1
print(myList2)
