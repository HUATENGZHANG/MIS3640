import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

import math
def quadratic(a, b, c):
    return x
x= (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
print(x)