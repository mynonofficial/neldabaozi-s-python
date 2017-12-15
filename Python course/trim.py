def trim(s):
    l = len(s)
    for n in range(l):
        if s[0] == " ":
            s = s[1:]
        if s[n] == " ":
            s = s[0:n-1] + s[(n+1):]
        else:
            s = s
    return s
print(trim("   Hello! "))
