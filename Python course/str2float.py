#from functools import reduce
#def str2float(L):
#    l = len(L)
#    c = 0
#    for n in range(l-1):
#        if L[n] == ".":
#            c = n
#            break
#    a = int(L[0:(c-2)])
#    b = int(L[c:(l-1)])
#    flonum = a + (0.1**(l-c))*b
#reduce(lambda x,y: x*10+y, map(xxx, L))
#print(str2float(["123.456"]))

from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10+y
    n = s.index(".")
    s1 = list(map(int, [x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n+1:]]))
    return reduce(fn, s1) + reduce(fn, s2)/(10**len(s2))
print("\"123.4567\"=",str2float("123.4567"))
