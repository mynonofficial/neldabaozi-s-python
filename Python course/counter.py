def generate_counter():
    CNT = [0]
    def add_one():
        CNT[0] = CNT[0] + 1
        return CNT[0]
    return add_one
counter = generate_counter()
print(counter())
print(counter())
print(counter())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
