def minus(s):
    return reduce(lambda x, y: x - y, s, 1)

def add(s):
    return reduce(lambda x, y: x + y, s, 1)

print minus(range(1,10))
print add(range(1,10))
