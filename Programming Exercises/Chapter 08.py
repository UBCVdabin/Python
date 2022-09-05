## 8.2
def main():
    first = input("Enter the first string: ").strip()
    second = input("Enter the second string: ").strip()
   
    if isSubstring(first, second) != -1: 
        print(first, "is a substring of", second)
    else:
        print(first, "is not a substring of", second)
        
# Check if the first string is a substring of the second string
def isSubstring(first, second):
    remainingLength = len(second)
    startingIndex = 0;

    while len(first) <= remainingLength:
        if first != second[startingIndex : startingIndex + len(first)]:
            startingIndex += 1
            remainingLength -= 1
        else:
            return startingIndex 

    return -1

main()

## 8.4
def main():
    s = input("Enter a string: ").strip()
    ch = input("Enter a character: ").strip()

    print(count(s, ch))

def count(s, ch):
    count = 0
    for c in s:
        if ch == c:
            count += 1
            
    return count
  
main()


## 8.6
def main():
    s = input("Enter a string: ").strip()

    print("The number of letters in " + s + " is " + str(count(s)))
   
def count(s):
    result = 0
    for c in s:
        if c.isalpha():
            result += 1
            
    return result
  
main()


## 8.8
def main():
    s = input("Enter a binary number string: ").strip().upper()
    print("The decimal value is " + str(binaryToDecimal(s)))

def binaryToDecimal(binaryString):
    value = ord(binaryString[0]) - ord('0')
    for i in range(1, len(binaryString)):
        value = value * 2 + ord(binaryString[i]) - ord('0')

    return value;

main()



## 8.10
def main():
    value = eval(input("Enter an integer: "))
    print("The binary value is " + str(decimalToBinary(value)))

def decimalToBinary(value):
    result = ""

    while value != 0:
        bit = value % 2;
        result = str(bit) + result
        value = value // 2

    return result

main()


## 8.12
def main():
    genome = input("Enter a genome string: ")
    
    found = False
    start = -1
    for i in range(len(genome) - 2):
        triplet = genome[i : i + 3]
        if triplet == "ATG":
            start = i + 3
        elif (triplet == "TAG" or triplet == "TAA" or triplet == "TGA") and start != -1:
            # A possible gene is found
            gene = genome[start : i]
            if len(gene) % 3 == 0:
                # A gene is found and display the gene
                found = True
                print(gene)  
                start = -1 # Start to find the next gene in the genome
    
    if not found:
        print("no gene is found")

main()


## 8.14
def main():
    number = input("Enter a credit card number as a string: ").strip()
    
    if isValid(number):
        print(number + " is valid")
    else:
        print(number + " is invalid")

# Return true if the card number is valid 
def isValid(number):
    return (number.startswith("4") or number.startswith("5") or
       number.startswith("6") or number.startswith("37")) and \
       (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0
  
# Get the result from Step 2
def sumOfDoubleEvenPlace(cardNumber):
    result = 0
    
    for i in range(len(cardNumber) - 2, -1, - 2):
        result += getDigit(int(cardNumber[i]) * 2)
    
    return result
  
# Return this number if it is a single digit, otherwise, return 
# the sum of the two digits 
def getDigit(number):
    return number % 10 + (number // 10 % 10)
  
# Return sum of odd place digits in number 
def sumOfOddPlace(cardNumber):
    result = 0

    for i in range(len(cardNumber) - 1, -1, -2):
        result += int(cardNumber[i])
    
    return result

main()


## 8.16
def main():
    number = input("Enter the first 12 digits of an ISBN as a string: ").strip()

    # Calculate checksum
    sum = 0
    for i in range(12):
        sum += int(number[i]) * (1 if i % 2 == 0 else 3) 

    checksum = 10 - sum % 10
    if checksum == 10: checksum = 0
    
    print("The ISBN-13 number is " + number + str(checksum))
    
main()


## 8.18
import math

def main():
    x1, y1, radius1 = eval(input("Enter x1, y1, radius1: "))
    x2, y2, radius2 = eval(input("Enter x2, y2, radius2: "))
    c1 = Circle2D(x1, y1, radius1)
    c2 = Circle2D(x2, y2, radius2)
    
    print("Area for c1 is", c1.getArea())
    print("Perimeter for c1 is", c1.getPerimeter())
    
    print("Area for c2 is", c2.getArea())
    print("Perimeter for c2 is", c2.getPerimeter())
    
    print("c1 contains the center of c2?", c1.containsPoint(c2.getX(), c2.getY()))
    print("c1 contains c2?", c1.contains(c2))
    print("c2 in c1?", c2 in c1)
    print("c1 overlaps c2?", c1.overlaps(c2))

    print("c1 < c2?", c1 < c2)
    
class Circle2D:
    def __init__(self, x = 0, y = 0, radius = 0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__radius
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y

    def setRadius(self, radius):
        self.__radius = radius
  
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def containsPoint(self, x, y):
        d = distance(x, y, self.__x, self.__y)
        return d <= self.__radius

    def contains(self, circle):
        d = distance(self.__x, self.__y, circle.__x, circle.__y)
        return d + circle.__radius <= self.__radius
  
    def overlaps(self, circle):
        return distance(self.__x, self.__y, circle.__x, circle.__y) \
            <= self.__radius + circle.__radius

    def __contains__(self, anotherCircle):
        return self.contains(anotherCircle)

    def __lt__(self, secondCircle): 
        return self.__cmp__(secondCircle) < 0

    def __le__(self, secondCircle): 
        return self.__cmp__(secondCircle) <= 0

    def __gt__(self, secondCircle): 
        return self.__cmp__(secondCircle) > 0

    def __ge__(self, secondCircle): 
        return self.__cmp__(secondCircle) >= 0
   
    # Compare two numbers
    def __cmp__(self, secondCircle): 
        if self.__radius > secondCircle.__radius:
            return 1
        elif self.__radius < secondCircle.__radius:
            return -1
        else:
            return 0        
        
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

main()




