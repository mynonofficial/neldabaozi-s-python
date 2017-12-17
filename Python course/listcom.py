def lowercase(L):
    M = [n.lower() for n in L if isinstance(n,str) == True]
    return M
print(lowercase(["Hello", "World", 18, "IBM", "Apple"]))
