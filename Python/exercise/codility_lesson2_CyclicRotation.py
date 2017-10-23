# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    if A == []:
        return A
    # write your code in Python 2.7
    result = [0]*len(A)

    if K > len(A):
        K = K % len(A)

    for i in range(len(A)):

        if (i+K) < len(A):
            result[i+K] = A[i]
        else:
            result[(i+K)-len(A)] = A[i]

    return result

print solution([0,1,2,3,4,5], 8)
