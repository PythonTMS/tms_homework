#You will be given a number and you will need to return it as a string in Expanded Form. For example:
#expanded_form(12) # Should return '10 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'


def expanded_form(num):
    a = str(num)
    b = []
    for i in range(len(a)):
        if a[i] == '0':
            continue
        b.append(a[i] + '0'*(len(a)-i-1))
    return " + ".join(b)


c = expanded_form(423499)
print(c)