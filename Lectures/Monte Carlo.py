import random
import math

def GetRandomCoordinate():
    x = random.randint(-100, 100)
    x /= 100
    return x

def DistanceToOrigin(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def DblEquals(val1, val2, epsilon = 0.000001):
    if abs(val1 - val2) < epsilon:
        return True
    else:
        return False

numberOfHits = 0
numberOfTries = 5000
for i in range(numberOfTries):
    pointX = GetRandomCoordinate()
    pointY = GetRandomCoordinate()
    dist = DistanceToOrigin(pointX, pointY)
    if dist < 1 or DblEquals(dist, 1):
        numberOfHits += 1

print(numberOfHits)
print("PI = " + str(4 * numberOfHits / numberOfTries))
