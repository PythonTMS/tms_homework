guests = int(input("Введите количество гостей:\n"))
if guests > 50:
    print("Ресторан")
elif 20 < guests < 50:
    print("Кафе")
elif guests < 20:
    print("Дом")
