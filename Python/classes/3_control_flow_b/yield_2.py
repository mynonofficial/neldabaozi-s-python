def nextSquare():
    i = 1;
    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1

# Driver code to test above generator function
# for num in nextSquare():
#     if num > 100:
#          break
#     print(num)

# x = nextSquare()
# print x.next()
