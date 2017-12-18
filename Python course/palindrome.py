#def is_palindrome(n):
#    strn = str(n)
#    l = len(strn)
#    s = 0
#    m = 0
#    for i in range(l):
#        s = s + int(strn[i])*(10**(l-i))
#    for i in range (l):
#        m = m + int(strn[i]*(10**i))
#    if s == m:
#        return n
#
#def primes():
#    seq = list(filter(is_palindrome(n),seq))
#for n in primes():
#    if n < 1000:
#        print(n)
#    else:
#        break
#
#print(primes(range(1,100)))
def is_palindrome(n):
    strn = str(n)
    if strn == strn[::-1]:
        return n
print(list(filter(is_palindrome,range(1,1000))))
