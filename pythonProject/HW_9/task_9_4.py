def reverse_order(func):
    def wrapper(*args):
        return func(*args[::-1])
    return wrapper


@reverse_order
def foo(*args):
    print(*args)


print(foo(1, 2, 3, 4, 5, 6, 7))
