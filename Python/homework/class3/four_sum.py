# Given four lists A, B, C, D of integer values,
# compute how many tuples (i, j, k, l) there are
# such that A[i] + B[j] + C[k] + D[l] is zero.

# To make problem a bit easier, all A, B, C, D
# All integers are in the range of -2^(28) to 2^(28 - 1)
# and the result is guaranteed to be at most 2^(31 - 1).

# Example:
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
def fourSumCount(A, B, C, D):
    target = 0
    # dictAB = {(A.index(x),B.index(y)):(x+y) for x in A for y in B}
    # dictCD = {(C.index(x),D.index(y)):(x+y) for x in C for y in D}
    # dictTarget_AB = {(target-(x+y):(A.index(x),B.index(y))) for x in A for y in B}

    dictAB = {}
    for i in range(len(A)):
        for j in range(len(B)):
            sumAB = A[i] + B[j]
            if sumAB in dictAB:
                dictAB[sumAB].append([i, j])
            else:
                dictAB[sumAB] = [[i,j]]
    # print dictAB

    result = []

    for i in range(len(C)):
        for j in range(len(D)):
            sumCD = C[i] + D[j]
            if -sumCD in dictAB:
                # pairCD = (i,j)
                for pairAB in dictAB[-sumCD]:
                    ai = pairAB[0]
                    bi = pairAB[1]
                    ci = i
                    di = j
                    result.append((ai,bi,ci,di))
    return result

    # dictCD = {}
    # for i in range(len(C)):
    #     for j in range(len(D)):
    #         sumCD = C[i] + D[j]
    #         if sumCD in dictCD:
    #             dictCD[sumCD].append((i,j))
    #         else:
    #             dictCD[sumCD] = [(i,j)]
    # # print dictCD
    #
    # result = []
    #
    # for key in dictAB.keys():
    #     if -key in dictCD:
    #
    #         # result.append((dictAB[key],dictCD[-key]))
    #         for pairAB in dictAB[key]:
    #             for pairCD in dictCD[-key]:
    #                 result.append((pairAB[0], pairAB[1], pairCD[0], pairCD[1]))
    # print result








    # CDkeys = dictCD.keys()
    # CDvalues = dictCD.values()
    # Target_ABkeys = dictTarget_AB.keys()
    # Target_ABvalues = dictTarget_AB.values()
    #
    # tuples = []
    #
    # for i in range(len(dictCD)):
    #     diff = target - CDvalue.[i]
    #     if diff in dictTarget_AB:


    # for i in range(0,len(dictCD),1):
    #     for j in range(0,len(dictCD),1):
    #         if Targe t_ABvalues[i] == CDvalues[j]:
    #             tuples.append((Target_ABkeys[i], CDkeys[j]))
    # return tuples

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print fourSumCount(A, B, C, D)
