## 10.1 점수 제일 잘 맞은 학생 기준으로 학점 매기기
'''
def getGrade(highestScore, score):
    if score >= highestScore - 10:
        return 'A'
    if score >= highestScore - 20:
        return 'B'
    if score >= highestScore - 30:
        return 'C'
    if score >= highestScore - 40:
        return 'D'
    else:
        return 'F'

def main():
    inputText = input("Enter scores: ")
    highestScore = 0
    alist = inputText.split()

    for i in range (len(alist)):
        if highestScore < int(alist[i]):
            highestScore = int(alist[i])

    for i in range (len(alist)):
        print("Student " + str(i) + " score is " + alist[i] + " and grade is " + getGrade(highestScore, int(alist[i])))

main()
'''




## 10.2 입력받은 숫자들 item 리스트에 주소값 저장 후 리버싱 돌려서 프린팅
'''
def main():
    # Read numbers as a string from the console
    s = input("Enter numbers separated by spaces from one line: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    numbers.reverse()
    print(numbers)
    
main()
'''



## 10.3 입력받은 숫자들 표현하는데 있어서 중복 숫자 카운팅
'''
def SelectionSort(aList):
    for i in range (len(aList) - 1):
        for j in range (i+1, len(aList)):
            if int(aList[i][0]) > int(aList[j][0]):
                aList[i], aList[j] = aList[j], aList[i]

def main():
    s = input("Enter integers between 1 and 100: ")
    alist = s.split()
    isExist = False
    rlist = []

    for item in alist:
        for i in range(len(rlist)):
            if rlist[i][0] == item:
                isExist = True
                break

        if isExist:
            isExist = False
            continue
        else:
            templist = [item, alist.count(item)]
            rlist.append(templist)

    SelectionSort(rlist)

    for item in rlist:
        print(item[0] + " ouccurs " + str(item[1]), end= " times\n" if item[1] > 1 else " time\n")

main()
'''



## 10.4 평균값 구하고 평균값보다 높은 숫자 카운팅, 낮은 숫자 카운팅, 그리고 프린팅
'''
def main():
    s = input("Enter the numbers: ") 
    items = s.split() # Extracts items from the string
    scores = [ eval(x) for x in items ] # Convert items to numbers

    numOfAbove = 0
    average = sum(scores) / len(scores)

    for score in scores:
        if score >= average:
            numOfAbove += 0

    print("Average is", average)
    print("Number of scores above or equal to the average", numOfAbove)
    print("Number of scores below the average", len(scores) - numOfAbove)

main()
'''




## 10.5 중복 숫자 제외하고 프린팅
'''
def main():
    s = input("Enter ten numbers: ")
    list1 = s.split()
    list2 = []
    isExist = False
    txt = ""

    for item in list1:
        for ritem in list2:
            if ritem == item:
                isExist = True
                break

        if isExist:
            isExist = False
            continue

        else:
            list2.append(item)

    for i in range(len(list2)):
        if i == len(list2) - 1:
            txt += list2[i]
        else:
            txt += list2[i] + " "

    print("The distinct numbers are: " + txt)

main() 
'''




## 10.6 숫자 50까지 소수 구하기
'''
import math

NUM_OF_PRIMES = 50
# Store prime numbers
primeNumbers = []

count = 0 # Count the number of prime numbers
number = 2 # A number to be tested for primeness
isPrime = True # Is the current number prime?

print("The first 50 prime numbers are \n")

# Repeatedly find prime numbers
while count < NUM_OF_PRIMES:
    # Assume the number is prime
    isPrime = True

    i = 0 
    while i < count and primeNumbers[i] <= math.sqrt(number):
        #If true, the number is not prime
        if number % primeNumbers[i] == 0:
            # Set isPrime to false, if the number is not prime
            isPrime = False
            break # Exit the for loop
        
        i += 1

    # Print the prime number and increase the count
    if isPrime:
        primeNumbers.append(number)
        count += 1 # Increase the count

        if count % 10 == 0:
            # Print the number and advance to the new line
            print(number)
        else:
            print(number, end = " ")

    # Check if the next number is prime
    number += 1
'''


## 10.7 랜덤 숫자 1000까지 받아서 개수 찍기
'''
import random

def main():
    alist = []
    for i in range (1000):
        alist.append(random.randint(0, 9))

    for i in range (10):
        print("The number of " + str(i) + " is " + str(alist.count(i)))

main()
'''




## 10.8 작은 숫자 판별 후 인덱스 보여주기
'''
def main():
    # Read numbers as a string from the console
    s = input("Enter scores separated by spaces from one line: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers

    print("The index of the smallest element is", indexOfSmallestElement(numbers))
   
def indexOfSmallestElement(list):
    min = list[0]
    minIndex = 0

    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
            minIndex = i

    return minIndex

main()
'''





## 10.10 리버스 함수 보면 인덱스 서로 교환하는 것을 볼수 있음
'''
def main():
    # Read numbers as a string from the console
    s = input("Enter numbers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    reverse(numbers)
    print(numbers)

def reverse(list):
    for i in range(len(list) // 2):
        list[i], list[len(list) -i -1] =  list[len(list) -i -1], list[i] 

    return list
        
main()
'''


## 10.12 최대 공약수 구하기
'''
import random

def main():
    # Read numbers as a string from the console
    s = input("Enter numbers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    
    print("The gcd of", numbers, "is", gcd(numbers))

def gcd(numbers):
    g = numbers[0]
    for i in range(1, len(numbers)):
        g = gcd2(g, numbers[i])

    return g

# Return the gcd of two integers 
def gcd2(n1, n2):
    g = 1 # Initial gcd is 1
    k = 2   # Possible gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            g = k # Update gcd
        k += 1

    return g # Return gcd
        
main()
'''



## 10.14 
## 문자열로 입력받은 다음 split으로 쪼개어 item list에 저장 후 number List 변수에 저장 (deep copy)
## 그 후 sort 한다. (shallow copy)
'''
import random

def main():
    # Read numbers as a string from the console
    s = input("Enter numbers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    selectionSort(numbers)
    print(numbers)

# The function for sorting the numbers 
def selectionSort(list):
    for i in range(len(list) - 1, 0, -1):
        # Find the minimum in the list[i..len(list)-1]
        currentMax = list[i]
        currentMaxIndex = i

        for j in range(i):
            if currentMax < list[j]:
                currentMax = list[j]
                currentMaxIndex = j

        # Swap list[i] with list[currentMinIndex] if necessary;
        if currentMaxIndex != i:
            list[currentMaxIndex] = list[i]
            list[i] = currentMax

main()
'''



## 10.15 문자열이 정렬된 상태로 되어있는 지 확인 코드
'''
def isSorted(lst):
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] < lst[i-1]:
            return False

    return True

def main():
    s = input("Enter list: ")
    lst = s.split()

    numbers = [eval(item) for item in lst ]

    if isSorted(numbers):
        print("The list is already sorted")
    else:
        print("The list is not sorted")

main()
'''


## 10.16 버블정렬 구현 코드
'''
def main():
    # Read numbers as a string from the console
    s = input("Enter numbers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    bubbleSort(numbers)
    print(numbers)
    
def bubbleSort(list):
    needNextPass = True
    
    k = 1
    while k < len(list) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(list) - k): 
            if list[i] > list[i + 1]:
                # swap list[i] with list[i + 1]
                list[i], list[i + 1] = list[i + 1], list[i]
          
                needNextPass = True # Next pass still needed           

main()
'''

## 10.18
def main():
    # Queen positions
    queens = 8 * [-1] # queens are placed at (i, queens[i])
    # -1 indicates that no queen is currently placed in the ith row
    
    queens[0] = 0 # Initially, place a queen at (0, 0) in the 0th row

    # k - 1 indicates the number of queens placed so far
    # We are looking for a position in the kth row to place a queen
    k = 1
    while k >= 0 and k <= 7:
      # Find a position to place a queen in the kth row
      j = findPosition(k, queens)
      if j < 0:
        queens[k] = -1
        k -= 1 # back track to the previous row
      else:
        queens[k] = j
        k += 1

    printResult(queens)


def findPosition(k, queens):
    start = 0 if queens[k] == -1 else (queens[k] + 1)

    for j in range(start, 8):
      if isValid(k, j, queens):
        return j # (k, j) is the place to put the queen now

    return -1

# Return true if you a queen can be placed at (k, j) 
def isValid(k, j, queens):
    # See if (k, j) is a possible position
    # Check jth column
    for i in range(k):
      if queens[i] == j:
        return False

    # Check major diagonal
    row = k - 1
    column = j - 1 
    while row >= 0 and column >= 0:
        if queens[row] == column:
            return False
        
        row -= 1
        column -= 1
          
    # Check minor diagonal
    row = k - 1
    column = j + 1 
    while row >= 0 and column <= 7:
        if queens[row] == column:
            return False

        row -= 1
        column -= 1
        
    return True

# Print a two-dimensional board to display the queens */
def printResult(queens):
    for i in range(8):
      print(str(i) + ", " + str(queens[i]))
    print()

    # Display the output
    for i in range(8):
      for j in range(queens[i]):
        print("| ", end = "")
      print("|Q|", end = "")
      
      for j in range(queens[i] + 1, 8):
        print(" |", end = "")
      print()
      
main()



## 10.20
def main():
    count = 0
    
    # Queen positions
    queens = 8 * [-1] # queens are placed at (i, queens[i])
    # -1 indicates that no queen is currently placed in the ith row
    
    queens[0] = 0 # Initially, place a queen at (0, 0) in the 0th row

    # k - 1 indicates the number of queens placed so far
    # We are looking for a position in the kth row to place a queen
    k = 1
    while k >= 0:
      # Find a position to place a queen in the kth row
      j = findPosition(k, queens)
      if j < 0:
        queens[k] = -1
        k -= 1 # back track to the previous row
      else:
        queens[k] = j
        if k == 7:
          count += 1 # One more solution found
          print("Solution" + str(count) + ":")
          printResult(queens)
        else:
          k += 1

    print("How many solutions?", count)

def findPosition(k, queens):
    start = 0 if queens[k] == -1 else (queens[k] + 1)

    for j in range(start, 8):
      if isValid(k, j, queens):
        return j # (k, j) is the place to put the queen now

    return -1

# Return true if you a queen can be placed at (k, j) 
def isValid(k, j, queens):
    # See if (k, j) is a possible position
    # Check jth column
    for i in range(k):
      if queens[i] == j:
        return False

    # Check major diagonal
    row = k - 1
    column = j - 1 
    while row >= 0 and column >= 0:
        if queens[row] == column:
            return False
        
        row -= 1
        column -= 1
          
    # Check minor diagonal
    row = k - 1
    column = j + 1 
    while row >= 0 and column <= 7:
        if queens[row] == column:
            return False

        row -= 1
        column -= 1
        
    return True

# Print a two-dimensional board to display the queens 
def printResult(queens):
    # Display the output
    for i in range(8):
      for j in range(queens[i]):
        print("| ", end = "")
      print("|Q|", end = "")
      
      for j in range(queens[i] + 1, 8):
        print(" |", end = "")
      print()
      
main()



## 10.22
import random

def main():
    NUMBER_OF_CARDS = 52
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
      "10", "Jack", "Queen", "King"]
    # found indicates whether a suit has been picked
    found = 4 * [False]

    # Count the number of picks
    numberOfPicks = 0
    
    # Count occurrence in each suit
    count = 0
    while count < 4:
      numberOfPicks += 1
      index = random.randint(0, NUMBER_OF_CARDS - 1)
      if not found[index // 13]:
          found[index // 13] = True
          count += 1
        
          suit = suits[index // 13]
          rank = ranks[index % 13]
          print(rank, "of", suit)
    
    print("Number of picks:", numberOfPicks)

main()



## 10.24
def main():  
    N = 10
    s = input("Enter ten integers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    
    for i in range(N): 
      for j in range(i + 1, N):
        print(numbers[i], numbers[j])

main()



## 10.26
def main():
    s = input("Enter list1: ") 
    items = s.split() # Extracts items from the string
    list1 = [ eval(x) for x in items ] # Convert items to numbers

    s = input("Enter list2: ") 
    items = s.split() # Extracts items from the string
    list2 = [ eval(x) for x in items ] # Convert items to numbers
    
    list3 = merge(list1, list2);
    
    print("The merged list is ", end = "")
    for e in list3:
        print(e, end = " ")

def merge(list1, list2):  
    result = []

    current1 = 0 # Current index in list1
    current2 = 0 # Current index in list2

    while current1 < len(list1) and current2 < len(list2):
      if list1[current1] < list2[current2]:
          result.append(list1[current1])
          current1 += 1
      else:
          result.append(list2[current2])
          current2 += 1

    while current1 < len(list1):
        result.append(list1[current1])
        current1 += 1

    while current2 < len(list2):
        result.append(list2[current2])
        current2 += 1

    return result

main()


## 10.28
def main():
    s = input("Enter a list: ") 
    items = s.split() # Extracts items from the string
    list = [ eval(x) for x in items ] # Convert items to numbers   
    
    partition(list)
    
    print("After the partition, the list is ", end = "")
    for e in list:
        print(e, end = " ")

def partition(list):
    pivot = list[0]  # Choose the first element as the pivot
    low = 1  # Index for forward search
    high = len(list) - 1  # Index for backward search

    while high > low:
        # Search forward from left
        while low <= high and list[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and list[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            list[high], list[low] = list[low], list[high]

    while high > 1 and list[high] >= pivot:
        high -= 1

    # Swap pivot with list[high]
    if pivot > list[high]:
        list[0] = list[high]
        list[high] = pivot

main()


## 10.30
def main():
    temp = year = eval(input("Enter a year: "))

    if year >= 1900:
        year -= 1900;
    else:
        year = 12 - (1900 - year) % 12
    
    animals = ["rat", "ox", "tiger", "rabbit", "dragon", 
      "snake", "horse", "sheep", "monkey", "rooster", "dog", "pig"]
 
    print(temp, "is", animals[year % 12])
    
main()


## 10.32
import turtle
import math

def drawLine(p1, p2):
    # turtle.setheading(0)

    # Compute the distance between p1 and p2
    d = math.sqrt((p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]))

    if p1[0] <= p2[0]: # p2 is on the right of p1
        angle = math.asin((p2[1] - p1[1]) / d)
    else:
        angle = -math.asin((p2[1] - p1[1]) / d) + math.pi

    turtle.penup()
    turtle.goto(p1[0], p1[1])
    turtle.pendown()
    turtle.radians()
    turtle.setheading(angle)
    turtle.forward(d)
 

## 10.34
import turtle
from RandomCharacter import *

def drawHistogram(list):
    WIDTH = 600 # Width of the histogram
    HEIGHT = 300 # Height of the histogram

    # Draw a base line
    turtle.penup()
    turtle.goto(-WIDTH / 2, -HEIGHT / 2)
    turtle.pendown()
    turtle.forward(WIDTH)

    widthOfBar = WIDTH / len(list) # Width of each bar

    for i in range(len(list)):     
        height = list[i] * HEIGHT / max(list) 
        drawABar(-WIDTH / 2 + i * widthOfBar + 10, 
            -HEIGHT / 2, widthOfBar - 5, height)     
        drawAString(-WIDTH / 2 + i * widthOfBar + 18, 
            -HEIGHT / 2 - 15, chr(i + ord('a')))   

    turtle.hideturtle()

def drawABar(i, j, widthOfBar, height):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90) # Set orientation to north
    turtle.pendown()

    turtle.forward(height) # Draw a vertical line
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(widthOfBar) # Draw a horizontal line
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(height) # Draw a vertical line

def drawAString(i, j, ch):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90) # Set orientation to north
    turtle.pendown()

    turtle.write(ch) 

count = 26 * [0]
for i in range(1000):
    ch = getRandomLowerCaseLetter()
    count[ord(ch) - ord('a')] += 1

drawHistogram(count)

turtle.done()


## 10.42
def main():
    s = input("Enter a string: ").strip()
    print("The sorted string is " + sort(s))

def sort(s):
    r = list(s)
    r.sort()
    
    result = ""
    for ch in r:
        result += ch
        
    return result

main()
