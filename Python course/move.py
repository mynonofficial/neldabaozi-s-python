import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.cos(angle)
    return nx, ny

print(move(100, 100, 60, (math.pi/6)))
