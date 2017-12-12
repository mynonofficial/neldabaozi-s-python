import math
def quadratic(a,b,c):
    if a == 0:
        return -c/b
    else:
        if b*b - 4*a*c < 0:
            return "none"
        else:
            if b*b - 4*a*c == 0:
                return -b/(2*a)
            else:
                return (-b - math.sqrt(b*b - 4*a*c), -b + math.sqrt(b*b - 4*a*C))

a = float(input('input a: '))
b = float(input('input b: '))
c = float(input('input c: '))
print (quadratic(a,b,c))
