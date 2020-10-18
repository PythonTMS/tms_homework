def delete_even(func):
    def wrapper(myList):
        for el in myList:
            if el % 2 == 0:
                myList.remove(el)
        return func(myList)
    return wrapper


@delete_even
def foo(myList):
    print(myList)


foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])