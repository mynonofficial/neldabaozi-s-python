def int2bin(i):
    if i == 0:
        return "0"
    s = ''
    while i != 0:
        if i % 2 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s

# Ex 1: With a pen and paper, manully compute the return value of some inputs
#  by following the exact steps as defined above
#  persuade yourself the above makes sense
#  Hint: the input is always an positive integer

# Ex 2: confirm the above implementation is correct for integers ranges from 0 to 99
#       or report case(s) where the above implementation is incorrect
#  Hint: python comes with a format function
#        e.g. "{0:b}".format(100) === "1100100"
