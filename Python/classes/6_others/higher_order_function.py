# Ref: https://wiki.haskell.org/Fold

# def f(x): return x % 3 == 0 or x % 5 == 0

# print filter(f, range(2, 25))
# print [ x for x in range(2, 25) if f(x)]

# def cube(x): return x*x*x
# # print map(cube, range(1, 11))
# # print [ cube(x) for x in range(1,11)]
#
# print filter(cube, range(1, 11))


def add(x, y): return x+y
def mult(x, y): return x*y
# print map(add, range(1,21), range(11,21))

# print zip(range(1,21), range(11,41))
def sum2(xs): return reduce(add, xs, 0)
# def prod2(xs): return reduce(mult, xs, 1)
def prod2(xs): return reduce(lambda x, y: x*y, xs, 1)
# print reduce(add, [1,2], 0)
# print sum2(range(10))
print prod2(range(1,10))
