# Given a list of integers, find k largest elements
# Assume that k is less than or equal to the length of the list
# The order of elements in the return list does not matter
# Hint:
#   Use Heap
import heapq

def topK(A,k):
    heap = []
    size = 0
    for a in A:
        if size < k:
            heapq.heappush(heap, a)
            size += 1
        else:
            top = heapq.heappop(heap)
            if top < a:
                heapq.heappush(heap, a)
            else:
                heapq.heappush(heap, top)
    return heap

# print topK([3213,23434,42,1,321],3)
print topK(range(10000),2)
