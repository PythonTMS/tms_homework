from math import sqrt
a = int(input("Введите длину первого катета\n"))
b = int(input("Введите длину второго катета\n"))
print("Гипотенуза: ", sqrt(a ** 2 + b ** 2), "\nПлощадь треугольника: ", (a + b) / 2)
