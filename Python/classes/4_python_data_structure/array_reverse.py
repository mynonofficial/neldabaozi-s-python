def reverse(A):
    N = len(A)
    for i in xrange(N / 2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]
    return A

list = range(1,10)
# reverse(list)
print reverse(list)
# list.reverse
# print list
