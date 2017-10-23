# Given a list of integers, find k largest elements
# Assume that k is less than or equal to the length of the list
# The order of elements in the return list does not matter
# Hint:
#   Recap the Quick Sort Algorithm
#   Could you do the problem in O(n) time?
def topK(A,k):
    result = []
    for i in range(k):
        result.append(max(A))
        A.remove(max(A))
    return result

print topK([3213,23434,42,1,321],3)
print topK(range(10000),2)
