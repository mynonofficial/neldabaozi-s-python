def findMinandMax(list):
    min = list[0]
    max = list [0]
    
    for a in list:
        if a < min or a == min:
            min = a
        elif a > max or a == max:
            max = a
    return (min, max)

print(findMinandMax([1,2,3,4,5]))
