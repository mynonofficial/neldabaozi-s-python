def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
    # return [1,2,3]

x = simpleGeneratorFun()
print x.next()
print x.next()
print x.next()
print x.next()

# for value in [1,2,3]:
# for value in simpleGeneratorFun():
#     print(value)
