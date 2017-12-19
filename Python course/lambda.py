def oddify(L):
    return list(filter(lambda x: x if x % 2 == 1 else None , L))

print(oddify(range(1,100)))
