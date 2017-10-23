def selectionSort(A):
    n = len(A)
    for k in xrange(n):
        minimal = k
        for j in xrange(k + 1, n):
            if A[j] < A[minimal]:
                minimal = j
        A[k], A[minimal] = A[minimal], A[k] # swap A[k] and A[minimal]
    return A
