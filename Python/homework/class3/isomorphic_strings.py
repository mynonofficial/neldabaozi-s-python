# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

def isIsomorphic(s, t):

    dict = {}
    for i in range(len(s)):
        x = s[i]
        y = t[i]
        # if x in dict:
        #     if dict[x] == y:
        #         continue
        #     else:
        #         return False
        # else:
        #     dict[s[i]] = t[i]
        if x in dict and dict[x] != y:
            return False
        else:
            dict[s[i]] = t[i]
        # dict[s] = t
    return True

    # dict = {s[i]:t[i] for i in range(len(s))}
    # print dict

    # # dict = {x:y for x in s for y in t if s.index(x) == t.index(y)}
    # l = len(s)
    # print dict
    #
    # for i in range(0,l,1):
    #     if t[i] == dict[s[i]]:
    #         continue
    #     else:
    #         return 'False'
    # return 'True'

print isIsomorphic('egg', 'add')
print isIsomorphic('foo', 'bar')
print isIsomorphic('paper', 'title')

print isIsomorphic('foog', 'barr')
