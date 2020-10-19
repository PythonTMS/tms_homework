#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of
#the other elements.


def move_zeros(array):
    array.sort(key=lambda el: el == 0 and el is not False)
    return array


a = move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9])
print(a)