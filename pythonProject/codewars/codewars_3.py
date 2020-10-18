#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
def phone_number(arr):
    a = "".join(map(str, arr))
    return f'({a[0:3]}) {a[3:6]}-{a[6:10]}'


c = phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(c)