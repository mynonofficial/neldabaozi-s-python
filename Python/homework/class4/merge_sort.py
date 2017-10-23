def merge(A, B):
    if len(A) == 0:
        return B
    if len(B) == 0:
        return A
    if A[0] <= B[0]:
        return [A[0]] + merge(A[1:], B)
    else:
        return [B[0]] + merge(A, B[1:])

def mergeSort(A):
    l = len(A)
    B = A[0:(l/2)]
    C = A[(l/2):]

    if B == []:
        return A

    sortedB = mergeSort(B)
    sortedC = mergeSort(C)
    return merge(sortedB, sortedC)

print mergeSort([2,1,4,3,6,5])
print mergeSort([7,6,5,4,3,2,1])
