myDict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for k in myDict.copy().keys():
    myDict[k + str(len(k))] = myDict[k]
    del myDict[k]
print(f'Измененный словарь:\n{myDict}')

print('----------------------------------------------------------------------------')

myDict1 = {}
keys = list(myDict.keys())
values = list(myDict.values())
i = 0
while i < len(keys):
    keys[i] = keys[i] + str(len(keys[i]))
    myDict1[keys[i]] = values[i]
    i += 1
print(myDict1)
