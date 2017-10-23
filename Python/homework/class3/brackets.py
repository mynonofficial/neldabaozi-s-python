# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[(()){}]{}" are all valid
# but "(]" and "([)]" are not.

def isValid(s):

    l = len(s)
    A = []

    for i in range(0,l,1):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            A.append(s[i])
            continue

        a = A.pop()

        if s[i] == ')':
            if a == '(':
                continue
            else:
                return 'Invalid'

        if s[i] == ']':
            if a == '[':
                continue
            else:
                return 'Invalid'

        if s[i] == '}':
            if a == '{':
                continue
            else:
                return 'Invalid'

    if A == []:
        return 'Valid'
    else:
        return 'Invalid'

print isValid('')
print isValid('()')
print isValid('()[(()){}]{}')
print isValid('([)]')
