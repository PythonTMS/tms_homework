# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of
# the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
#Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.


def narcissistic(value):
    summ = 0
    for el in str(value):
        summ += int(el)**len(str(value))
    if summ == value:
        return True
    return False


a = narcissistic(371)
print(a)