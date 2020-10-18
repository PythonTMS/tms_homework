fib = []
a = 0
b = 1
for i in range(0, 15):
    a, b = b, a+b
    fib.append(a)
print(fib)

print('---------------------------')

fib1 = []
a1 = 0
b1 = 1
i = 0
while i < 15:
    a1, b1 = b1, a1 + b1
    fib1.append(a1)
    i += 1
print(fib1)
