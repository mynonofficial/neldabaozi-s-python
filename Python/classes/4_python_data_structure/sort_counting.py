def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in xrange(n):
        count[A[i]] += 1
    p = 0
    # print 'count', count
    result = [0] * len(A)
    for i in xrange(k + 1):
        for j in xrange(count[i]):
            # print 'i', i, 'j', j, 'p', p
            result[p] = i
            p += 1
            # print p
            # print A[p], '---'
    return result
print countingSort([6,2,6,5,1,2,3,4],8)
