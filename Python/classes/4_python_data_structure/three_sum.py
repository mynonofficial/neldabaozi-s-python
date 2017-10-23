# Given an array S of n integers, are there elements a, b, c in S such that
# a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# A triplet is a list that contains 3 elements.
# Note: The solution set must not contain duplicate triplets.
#       Order of numbers in each triplets does not matter

# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
def threeSum(nums):

    dict1 = {}

    for i in range(len(S)):
        for j in range(i+1,len(S)):
            sum12 = S[i] + S[j]
            if sum12 in dict1:
                dict1[sum12].append([i,j])
            else:
                dict1[sum12] = [[i,j]]

    result = set()

    for i in range(len(S)):
        if -S[i] in dict1:
            for pair in dict1[-S[i]]:
                tuple = [S[i],S[pair[0]],S[pair[1]]]
                tuple.sort()
                a = tuple[0]
                b = tuple[1]
                c = tuple[2]
                if i > pair[0] and \
                    i > pair[1]:
                    result.add((a, b, c))

    return [list(x) for x in result]

S = [-1, 0, 1, 2, -1, -4]
print threeSum(S)
