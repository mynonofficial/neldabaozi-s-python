# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[(()){}]{}" are all valid
# but "(]" and "([)]" are not.

def isValid(s):
    A = []
    dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for i in range(0,len(s),1):
        if s[i] in dict:
            if len(A) == 0:
                return 'Invalid'
            a = A.pop()
            if a == dict[s[i]]:
                continue
            else:
                return 'Invalid'
        else:
            A.append(s[i])
            continue

    if A == []:
        return 'Valid'
    else:
        return 'Invalid'

print isValid('')
print isValid('()')
print isValid('()[(()){}]{}')
print isValid('([)]')
