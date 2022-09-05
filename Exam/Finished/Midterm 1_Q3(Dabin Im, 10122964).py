import math

def ForceBetweenTwoObjects(m1, m2, r):
    G = 6.67 * 10**-11 
    F = G * (m1 * m2) / (r**2) 
    return F

print(ForceBetweenTwoObjects(10, 20, 200))
print(ForceBetweenTwoObjects(1, 200, 20))


def Force(m1, m2, r):
    g = 6.67 * 10 ** (-11)
    return (g * m1 * m2) / r ** 2

print(Force(10, 20, 200)) ##outputs 
print(Force(1, 200, 20)) ##outputs 
