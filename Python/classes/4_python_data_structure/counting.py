# count the occurrance of an element in an arrary / a list

def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in xrange(n):
        count[A[k]] += 1
    return count

def dictCounting(A):
    dict = {}
    for a in A:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1
    return dict

def count(dict, m):
    if m in dict:
        return dict[m]
    return 0
# Test
A = [1,4,8,7]
dict = dictCounting(A)
print dict
print count(dict, 7)
print count(dict, 15)

# Exercise
# You are given an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed
# arrays A and B of n integers, a(0), a(1), ... , a(n-1) and
# b(0), b(1), ... , b(n-1) respectively (0 <= a(i), b(i) <= m).
# The goal is to check whether there is a swap operation which can be performed
# on these arrays in such a way that the sum of elements in array A equals the
# sum of elements in array B after the swap. By swap operation we mean picking
# one element from array A and one element from array B and exchanging them

def slow_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in xrange(n):
        for j in xrange(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False

def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    if d % 2 == 1:
        return False
        d /= 2
        count = counting(A, m)
    for i in xrange(n):
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            return True
    return False
