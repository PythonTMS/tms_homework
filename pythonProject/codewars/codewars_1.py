#Implement the function unique_in_order which takes as argument a sequence and returns a list of items
#without any elements with the same value next to each other and preserving the original order of
#elements.
def unique_in_order(iterable):
    a = ""
    lst = []
    for i in iterable:
        if i != a:
            lst.append(i)
        a = i
    return lst


print(unique_in_order(('AAAAABBBBBCCCAAAAFFFDDD')))
