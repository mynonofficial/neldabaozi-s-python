def by_name(t):
    return t[0].lower()
L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Cisa", 88)]
L1 = sorted(L, key=by_name)
print(L1)

def by_score(t):
    return t[1]
L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Cisa", 88)]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)
