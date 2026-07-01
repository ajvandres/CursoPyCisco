import math, sys

print(math.sin(math.pi/2))
print()

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
    
print(sin(pi/2))
print(math.sin(math.pi/2))