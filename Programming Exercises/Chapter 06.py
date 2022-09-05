## Chapter 6에서 계속 봐야할 것들 (문제: )
# 알게된 것들 
# 소수 구하기 : 에라토스테네스의 체, 해당 숫자에서 반만 비교하기, Mersenne prime(?)

## 6.1 재귀 함수
'''
def getPentagonalNumber(n):
    if n < 5:
        print(n * (3*n - 1) / 2)
        n += 1
        return getPentagonalNumber(n)
    
getPentagonalNumber(1)
'''


## 6.2 재귀 함수 
'''
def sumDigits(n, sum = 0):
    
    sum += n % 10
    
    n = n // 10
    if n > 0:
        return sumDigits(n, sum)
    else:
        return sum


print(sumDigits(234))
'''

## 6.2 교수님 정답
'''
def GetLastDigit(n):
    lastDigit = n % 10
    return lastDigit

def sumDigits(n):
    total = 0
    while n > 0:
        digit = GetLastDigit(n)
        total += digit
        n = n // 10
    return total

def main():
    x = sumDigits(789)
    print(x) ## 24

main()
'''




## 6.3 기존 입력된 숫자가 Palindrome인지 판별 후 프린팅
'''
def isPalindrome(n):
    if n == reverse(n):
        return True
    else:
        return False

def reverse(n, sum = 0):
    
    sum *= 10
    sum += n % 10
    
    n = n // 10
    if n > 0:
        return reverse(n, sum)
    else:
        return sum

print("This number is ", end= "Palindrome!\n" if isPalindrome(456) else "not Palindrome...\n")
'''





## 6.4 숫자 반대로 바꾼 뒤 보여주기
'''
def reverse(n, sum = 0):
    
    sum *= 10
    sum += n % 10
    
    n = n // 10
    if n > 0:
        return reverse(n, sum)
    else:
        return sum

print(reverse(3456))
'''




## 6.5 숫자 낮은순으로 정렬하여 표현하기
'''
def displaySortedNumbers(num1, num2, num3):
    if num1 < num2:
        num1, num2 = num2, num1

    if num1 < num3:
        num1, num3 = num3, num1
        
    if num2 < num3:
        num2, num3 = num3, num2 
    
    return num3, num2, num1

num1, num2, num3 = eval(input("Enter three numbers: "))
num1, num2, num3 = displaySortedNumbers(num1, num2, num3)
print("The sorted numbers are", num1, num2, num3) 
'''


## 6.6 숫자 찍기
#    1
#   21
#  321
# 4321
#54321
'''
def countDigits(n):
    count = 1
    while n // 10 > 0:
        count += 1 
        n //= 10
    return count


def displayPattern(n):
    strDigitsCount = str(countDigits(n)) + "d" 
    strSpaceCount = str(countDigits(n)) + "s" 
    for i in range (0, n, 1):
        for j in range (i + 1, n):
            print(format(" ", strSpaceCount), end = " ")
        for j in range (i + 1, 0, -1):
            print(format(j, strDigitsCount), end =" ")
        print()

displayPattern(60)
'''




## 6.7 투자한 후에 이자율 계산하여 이익 금액 계산하기
'''
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    investmentAmount = investmentAmount * (1 + monthlyInterestRate)**(years * 12)
    return investmentAmount


amount = eval(input("The amount invested: "))
interestRate = eval(input("Annual interest rate: "))
monthlyRate = interestRate * 1/1200
print("Years\tFuture Value")

for i in range(1, 31):
    print(str(i) + "\t   " + format(futureInvestmentValue(amount, monthlyRate, i), "6.2f"))
'''






## 6.8 화씨, 섭씨 온도 동시에 보여주기
'''
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32
def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

print("Celsius      Fahrenheit  |  Fahrenheit      Celsius")

for i in range(10, 0, -1):
    print(format(30 + i, "5.1f") + "          " + format(celsiusToFahrenheit(30 + i), "5.1f")  + \
        "     |    " + format(20 + (i * 10), "5.1f") + "         " + format(fahrenheitToCelsius(20 + (i * 10)), "5.1f"))
'''





## 6.9 feet과 meter 를 동시에 보여주기
'''
def footToMeter(foot):
    return 0.305 * foot

def meterToFoot(meter):
    return meter / 0.305

print("Feet          Meters     |   Meters          Feet")

for i in range(1, 11, 1):
    print(format(i, "4.1f") + "           " + format(footToMeter(i), "5.1f")  + \
        "     |    " + format(14 + (i * 6), "5.1f") + "         " + format(meterToFoot(14 + (i * 6)), "5.1f"))
'''





## 6.10 10000 이하의 소수 찾은 뒤에 개수 찍기
'''
def main():
    count = 0
    N = 10000
    for number in range(2, N):
        if isPrime(number):
            count += 1

    print("The number of prime number <", 10000, "is", count)

# Check whether number is prime 
def isPrime(number):
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0: # If true, number is not prime
            return False # number is not a prime

    return True # number is prime

main()
'''





## 6.11 연봉 커미션 문제
'''
def GetCommission(salesAmount):
    if salesAmount >= 0 and salesAmount <= 5000:
        return  salesAmount * 0.08
    elif salesAmount > 5000 and salesAmount <= 10000:
        return 5000 * 0.08 + (salesAmount - 5000) * 0.10
        # return salesAmount * 0.10
    else:
        return 5000 * 0.08 + 5000 * 0.10 + (salesAmount - 10000) * 0.12
        # return salesAmount * 0.12

def main():
    for i in range(1, 21):
        print(5000 + i * 5000, "\t\t", GetCommission(5000 + i * 5000))

main()
'''





## 6.12 문자 두개 입력 받아서 차례대로 문자들을 출력함 
'''
def printChars(ch1, ch2, numberPerLine = 10):
    count = 1

    for i in range(ord(ch1), ord(ch2)):
        if count % numberPerLine == 0:
            print(chr(i))
            count = 1
        else:
            print(chr(i), end= " ")
            count += 1
    print()

def main():
    ch1 = input("Enter the first character: ")
    ch2 = input("Enter the second character: ")
    printChars(ch1, ch2)

main()
'''





## 6.13 등차수열 문제 (공비가 바뀜)
'''
def sumSeries(index):
    sum = 0
    for i in range(1, (index+1)):
        sum += i / (i + 1)
    return sum

for i in range(1, 21):
    print(str(i) + "\t\t" + format(sumSeries(i), "6.4f"))
'''





## 6.14 공식을 이용하여 PI 유도하기 
'''
def EstimatePI(index):
    sum = 0
    for i in range(1, (index+1)):
        sum += (-1)**(i+1) / (2 * i - 1)
    return 4 * sum

for i in range(1, 1000, 100):
    print(str(i) + "\t\t " + format(EstimatePI(i), "5.4f"))
'''





## 6.15 세금 계산하기
'''
import sys

def computeTax(status, income):

    # Compute tax
    tax = 0

    if tax > 3 or tax < 0:  
        print("Error: invalid status")
        sys.exit()

    if status == 0:  # Compute tax for single filers
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 8350 * 0.10 + (income - 8350) * 0.15
        elif income <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (income - 33950) * 0.25
        elif income <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (82250 - 33950) * 0.25 + (income - 82250) * 0.28
        elif income <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
                (income - 171550) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
                  (372950 - 171550) * 0.33 + (income - 372950) * 0.35

    elif status == 1: # Compute tax for married file jointly
        if income <= 16700:
            tax = income * 0.10
        elif income <= 67900:
            tax = 16700 * 0.10 + (income - 16700) * 0.15
        elif income <= 137050:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                (income - 67900) * 0.25
        elif income <= 208850:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                (137050 - 67900) * 0.25 + (income - 82250) * 0.28
        elif income <= 372950:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                (137050 - 67900) * 0.25 + (208850 - 82250) * 0.28 + \
                (income - 208850) * 0.33
        else:
            tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
                  (82250 - 33950) * 0.25 + (208850 - 82250) * 0.28 + \
                  (372950 - 208850) * 0.33 + (income - 372950) * 0.35

    elif status == 2: # Compute tax for married separately
        if income <= 8350:
            tax = income * 0.10
        elif income <= 33950:
            tax = 8350 * 0.10 + (income - 8350) * 0.15
        elif income <= 68525:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (income - 33950) * 0.25
        elif income <= 104425:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (68525 - 33950) * 0.25 + (income - 68525) * 0.28
        elif income <= 186475:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
                (income - 104425) * 0.33
        else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
                  (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
                  (186475 - 104425) * 0.33 + (income - 186475) * 0.35

    else: # Compute tax for head of household
        if income <= 11950:
            tax = income * 0.10
        elif income <= 45500:
            tax = 11950 * 0.10 + (income - 11950) * 0.15
        elif income <= 117450:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                (income - 45500) * 0.25
        elif income <= 190200:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                (117450 - 45500) * 0.25 + (income - 117450) * 0.28
        elif income <= 372950:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
                (income - 190200) * 0.33
        else:
            tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
                  (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
                  (372950 - 190200) * 0.33 + (income - 372950) * 0.35

    return tax 



# Display the result
def main():
    status = eval(input(
    "(0-single filer, 1-married jointly,\n" +
    "2-married separately, 3-head of household)\n" +
    "Enter the filing status: "))

# Prompt the user to enter taxable income
    income = eval(input("Enter the taxable income: "))
    print("Tax is", format(computeTax(status, income), ".2f"))

main()
'''





## 6.16 윤년 계산 다시 확인하기 
#       윤년 계산하기 
#       조건 1) 해당년도 % 400 = 0 (예: 2000년)
#       조건 2) 해당년도 % 4 = 0 and 해당년도 % 100 != 0 인 경우.
#       두 조건 중 한가지만 성립해도 윤년! 
'''
def numberOfDaysInAYear(year):
    if isLeapYear(year):
      return 366
    else:
      return 365

# Determine if it is a leap year *
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    for year in range(2010, 2020 + 1):
        print(year, "has", numberOfDaysInAYear(year))

main()
'''



## 6.17 삼각형의 조건 
#       가장 큰 길이인 a 가 존재할 경우, 
#       a < b + c 가 무조건 성립해야한다.
'''
import math

def isValid(side1, side2, side3):
    if side1 < side2:
        side1, side2 = side2, side1 
    if side1 < side3:
        side1, side3 = side3, side1
    
    if side1 >= side2 + side3:
        return False
    else:
        return True

def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

def main():
    side1, side2, side3 = eval(input("Enter three sides in double: "))
    if isValid(side1, side2, side3):
        print("The area of the triangle is " + str(area(side1, side2, side3)))
    else:
        print("Input is invalid")
main()
'''



## 6.18 랜덤 함수 이용해서 행렬 매트릭스 만들기 
'''
import random
def printMatrix(n):
    for i in range (1, n + 1):
        for j in range (1, n + 1):  
            print(random.randint(0,1), end= " ")
        print()

def main():
    printMatrix(eval(input("Enter n: ")))

main()
'''



## 6.19 백터 내적(?)을 이용한 직선을 기준하여 점의 위치 파악하기 -> 공식 이해 필요함..
'''
def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) > 0:
        return True
    return False

def rightOfTheLine(x0, y0, x1, y1, x2, y2):
    if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) < 0:
        return True
    return False

def onTheSameLine(x0, y0, x1, y1, x2, y2):
    if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0\
        and (x1 + x0) / 2 == x2 and (y1 + y0) / 2 == y2:
        return True
    return False

def onTheLineSegment(x0, y0, x1, y1, x2, y2):
    if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0:
        return True
    return False

def main():
    x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

    if onTheSameLine(x0, y0, x1, y1, x2, y2):
        print("p2 is on the same line from p0 to p1")

    if leftOfTheLine(x0, y0, x1, y1, x2, y2):
        print("p2 is on the left side of the line from p0 to p1")

    if rightOfTheLine(x0, y0, x1, y1, x2, y2):
        print("p2 is on the right side of the line from p0 to p1")

    if onTheLineSegment(x0, y0, x1, y1, x2, y2):
        print("p2 is on the line segment from p0 to p1")

main()
'''



## 6.20 3개의 직선을 가지고 각도 구하기 ( 각도 구하는 공식 모름...)
'''
import math

def main():
    x1, y1, x2, y2, x3, y3 = eval(input("Enter three points: "))
     
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)
    
    A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
    B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
    C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

    print("The three angles are", round(A, 2), round(B, 2), round(C, 2))

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

main()
'''



## 6.21 이거 루트 구하는 공식
# 바빌로니안 방법과, 뉴턴-랩슨 공식이 있다. 
'''
def DblEquals(val1, val2, epsilon = 0.001):
    if abs(val1 - val2) < epsilon:
        return True
    else:
        return False

def sqrt(n):
    lastGuess = 1
    while True:
        nextGuess = (lastGuess + (n / lastGuess)) / 2  ##babylonian function
        if DblEquals(lastGuess, nextGuess):
            return nextGuess
        else:
            lastGuess = nextGuess

def main():
    n = 5
    print(sqrt(n))
    print(n**0.5)

main()
'''



## 6.22   문제 분석 결과 : time.time()은 1970년 1월 1일부터 시작한다.
#                         따라서, 현재 일수와 시간을 구하기에 초 -> 분 -> 시간 -> 일로 구한 뒤에
#                         1970년에서 시작하여 현재 년도까지의 총 일수를 구하고 비교한다.
#                         즉, time.time() 함수로 이용하여 구해낸 날짜가 1970년부터 시작하여 모든 날짜(=365일 또는 366일[윤년])를 더한 값보다 작을 경우의
#                         해당 년도를 찾음
#                         마찬가지로 동일한 방법으로 month 와 day를 찾아낸 뒤 프린팅한다.              
'''
import time

def main():
    currentTime = time.time() # Get current time

    # Obtain the total seconds since midnight, Jan 1, 1970
    totalSeconds = int(currentTime)

    # Get the current second 
    currentSecond = totalSeconds % 60 

    # Obtain the total minutes
    totalMinutes = totalSeconds // 60 

    # Compute the current minute in the hour
    currentMinute = totalMinutes % 60

    # Obtain the total hours
    totalHours = totalMinutes // 60

    # Compute the current hour
    currentHour = totalHours % 24

    # Compute the total days
    totalDays = totalHours // 24
    if currentHour > 0:
        totalDays += 1

    # Obtain Year
    currentYear = 2000
    while getTotalDaysInYears(currentYear) < totalDays:
        currentYear += 1

    # Obtain Month
    totalNumOfDaysInTheYear = totalDays - getTotalDaysInYears(currentYear - 1);
    currentMonth = 0;
    while getTotalDaysInMonths(currentYear, currentMonth) < totalNumOfDaysInTheYear:
        currentMonth += 1

    # Obtain Day
    currentDay = totalNumOfDaysInTheYear - getTotalDaysInMonths(currentYear, currentMonth - 1)

    # Display results
    output = "Current date and time is " + \
        str(currentMonth) + "/" + str(currentDay) + "/" + str(currentYear) + " " + \
        str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond) + " GMT"

    print(output)


#Get the total number of days from Jan 1, 1970 to the specified year
def getTotalDaysInYears(year):      
    total = 0

    # Get the total days from 1970 to the specified year
    for i in range(1970, year + 1):
        if isLeapYear(i):
            total = total + 366
        else:
            total = total + 365

    return total


# Get the total number of days from Jan 1 to the month in the year*
def getTotalDaysInMonths(year, month):
    total = 0

    # Add days from Jan to the month
    for i in range(1, month + 1):
        total = total + getNumberOfDaysInMonth(year, i)

    return total

# Get the number of days in a month
def getNumberOfDaysInMonth(year, month): 
    if month == 1 or month == 3 or month == 5 or month == 7 or \
        month == 8 or month == 10 or month == 12:
        return 31

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if month == 2:
        return 29 if isLeapYear(year) else 28

    return 0 # If month is incorrect

# Determine if it is a leap year
def isLeapYear(year): 
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

main()
'''



## 6.23 밀리초 값으로 시간 찍기
'''
def convertMillis(millis):

    millis //= 1000
    
    seconds = millis % 60
    millis //= 60
    miniutes = millis % 60
    millis //= 60
    hours = millis

    print(str(hours) + ":" + str(miniutes) + ":" + str(seconds))

def main():
    convertMillis(5500)
    convertMillis(100000)
    convertMillis(555550000)

main()
'''



## 6.24 소수 판별과 Palindrome 통합 비교 후에 프린팅
'''
def main():
    count = 1

    i = 2 
    while count <= 1000:
        # Display each number in five positions
        if isPrime(i) and isPalindrome(i):
            print(i, end = " ")

            if count % 10 == 0:
                print()

            count += 1 # Increase count
        
        i += 1

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

# Return the reversal of an integer, i.e. reverse(456) returns 654
def isPalindrome(number):
    return number == reverse(number)


def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result

main()
'''



## 6.25 소수 계산하면서 reverse 한다음 숫자가 동일하지 않는 경우에만 찍는 케이스
#       Key Point: if isPrime(i) and isPrime(reverse(i)) and i != reverse(i):
'''
def main():
    count = 1

    i = 2 
    while count <= 100:
        # Display each number in five positions
        if isPrime(i) and isPrime(reverse(i)) and i != reverse(i):
            print(i, end = " ")

            if count % 10 == 0:
                print()

            count += 1 # Increase count
        
        i += 1

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

# Return the reversal of an integer, i.e. reverse(456) returns 654
def isPalindrome(number):
    return number == reverse(number)


def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result

main()
'''



## 6.26 Mersenne prime 룰 이용해서 소수 구하기
#       단, 짝수이자 소수인 2의 배수로만 판단 가능함 [단점]
#       예) 2 ** p - 1 <- Mersenne prime [3, 7, 31 ...]    
'''
import time

def main():
    beginTime = time.time()
    
    for p in range(2, 31 + 1):
      i = 2 ** p - 1            # <- Mersenne prime [3, 7, 31 ...]

      # Display each number in five positions
      if isPrime(i):
          print(p, "\t", i)

    endTime = time.time()
    print("Time spent is", endTime - beginTime, "milliseconds")

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime


def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result

main()
'''



## 6.27 선생님이 알려주신 소수 구하기 방법 (시간 복잡도를 염두한 방법이다)
#                                       range(2, int(n**0.5 + 1))
'''
def isPrime(n):
    for i in range (2, int(n**0.5 + 1)):
        if n % i == 0:
            return False

    return True

def main(): 
    for i in range(3, 1000):
        if isPrime(i) and isPrime(i + 2): # (i + 2) <- differ by 2
            print("(" + str(i) + ", " + str(i+2) + ")")

main()
'''



## 6.28 카지노 게임 Craps (룰: 처음 주사위 2개를 던졌을 때, 두개의 합 => 승리: 7, 11  패배: 2, 3, 12
#                             만약 이외의 숫자가 나왔을 경우 그 숫자를 기준점으로 잡는다. 예) point = 8
#                             이제 숫자 8이 나오면 승리 !  
#                             7이 나오면 패배하는 방식이다.)
'''
import random
import sys

def main():
    dice = getDice()
    if dice == 7 or dice == 11:
        print("You win")
        sys.exit()
    elif dice == 2 or dice == 3 or dice == 12:
        print("You lose")
        sys.exit()

    point = dice
    print("point is", point)
    
    dice = getDice()
    while dice != 7 and dice != point:
        dice = getDice()
    
    if dice == 7:
        print("You lose")
    else:
        print("You win")

# Get a dice
def getDice():
    i1 = random.randint(1, 6)
    i2 = random.randint(1, 6)

    print("You rolled", i1, "+", i2, "=", i1 + i2)
    return i1 + i2

main()
'''



## 6.29 -> 신용카드 유효성 검사 문제
'''
import sys
def isValid(number):
    if number % 10 == 0:
        return True
    else:
        return False

def sumOfDoubleEvenPlace(number, digits):
    sum = 0
    for i in range(1 , digits + 1, 1):
        if i % 2 == 0:
            sum += getDigit(number % 10)

        number = number // 10

    return sum

def getDigit(number):
    number = number * 2
    result = number
    if number >= 10:
        result = number // 10
        result += number % 10
    return result

def sumOfoddPlace(number, digits):
    sum = 0
    for i in range(1 , digits + 1, 1):
        if i % 2 != 0:
            sum += number % 10

        number = number // 10
    return sum

def prefixMatched(number, d):

    if getPrefix(number, d) == 4:
        return True                                                     ## Visa card
    elif getPrefix(number, d) == 5:
        return True                                                     ## MarsterCard
    elif getPrefix(number, d) == 6:
        return True                                                     ## Discover card
    elif getPrefix(number, d) == 3 and getPrefix(number, d-1) == 7: 
        return True                                                     ## 37 -> American Express card                                    
    else:
        return False

def getPrefix(number, k):
    return number // 10**k

def getSize(d):
    count = 0
    while d > 0:
        count += 1
        d //= 10 
    return count

def getCardMaker(number, d):
    if getPrefix(number, d) == 4:
        return "Visa Card"
    elif getPrefix(number, d) == 5:
        return "Marster Card"
    elif getPrefix(number, d) == 6:
        return "Discover Card"
    else: 
        return "American Express Card"


def main():
    number = eval(input("Enter card number: "))
    digits = getSize(number)
    if digits > 17 or digits < 13:
        print("This card is invaild.")
        sys.exit(0)

    if not prefixMatched(number, digits - 1):      ## n - 1 => 마지막 숫자 제외
        print("This card is invaild.")
        sys.exit(0)

    if isValid(sumOfoddPlace(number, digits) + sumOfDoubleEvenPlace(number, digits)):
        print("Result      : This Card is Vaild!")
        print("Card Name   : " + getCardMaker(number, digits - 1))
        print("Card Number : " + str(number))
    else:
        print("This card is invaild.")

main()
'''



## 6.30 -> 문제 28번과 동일한 카지노 게임 Craps 
##         카지노 게임 Craps (룰: 처음 주사위 2개를 던졌을 때, 두개의 합 => 승리: 7, 11  패배: 2, 3, 12
#                                만약 이외의 숫자가 나왔을 경우 그 숫자를 기준점으로 잡는다. 예) point = 8
#                                이제 숫자 8이 나오면 승리 !  
#                                7이 나오면 패배하는 방식이다.)
#          이번에는 10000판 중에서 몇 번 이겼는지 표현하는 방법이다. 따라서 확률도 구할 수 있다.
''' 
import random
import sys

def main():
    winCount = 0

    for i in range(10000):
        dice = getDice()
        if dice == 7 or dice == 11:
            winCount += 1
        elif dice == 2 or dice == 3 or dice == 12:
            winCount += 0
        else:
            point = dice
            dice = getDice()
            # print("point is " + str(point))
            while dice != 7 and dice != point:
                dice = getDice()
            
            if dice != 7:
                winCount += 1

    print(winCount)
       
# Get a dice
def getDice():
    i1 = random.randint(1, 6)
    i2 = random.randint(1, 6)

    # print("You rolled " + str(i1) + " + " + str(i2) + " = " + str(i1 + i2))
    return i1 + i2

main()
'''



## 6.31



## 6.32 -> 교재에 있는 Zeller's congruence를 이용해서 해당하는 달력을 찍는 것이다.
#       -> 내가 풀었던 5.31 과 비슷한 문제라고 생각하면 됨
'''
def printMonth(year, month): 
    # Print the headings of the calendar
    printMonthTitle(year, month)

    # Print the body of the calendar
    printMonthBody(year, month)
  
# Print the month title, e.g., May, 1999
def printMonthTitle(year, month): 
    print("         ", getMonthName(month), year)
    print("-----------------------------")
    print(" Sun Mon Tue Wed Thu Fri Sat")

# Print month body 
def printMonthBody(year, month): 
    # Get start day of the week for the first date in the month
    startDay = getStartDay(year, month)

    # Get number of days in the month
    numberOfDaysInMonth = getNumberOfDaysInMonth(year, month)

    # Pad space before the first day of the month
    i = 0
    for i in range(startDay):
       print("    ", end = "")

    for i in range(1, numberOfDaysInMonth + 1):
        print(format(i, "4d"), end = "")

        if (i + startDay) % 7 == 0:
            print() # Jump to the new line

# Get the English name for the month
def getMonthName(month): 
    monthName = ""
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8: 
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    else:
        monthName = "December"

    return monthName

# Get the start day of month/1/year 
def getStartDay(year, month): 
    if month == 1:
        month = 13
        year = year - 1 # January is counted as month 13 of the previous year.
    elif month == 2:
        month = 14
        year = year - 1 # February is counted as month 14 of the previous year.
        
    j = year // 100
    k = year % 100
        
    dayOfMonth = 1
    dayOfWeek = (dayOfMonth + 26 * (month + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7
    
    return (dayOfWeek + 6) % 7


# Get the number of days in a month
def getNumberOfDaysInMonth(year, month): 
    if (month == 1 or month == 3 or month == 5 or month == 7 or
        month == 8 or month == 10 or month == 12):
        return 31

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if month == 2:
        return 29 if isLeapYear(year) else 28

    return 0 # If month is incorrect

# Determine if it is a leap year
def isLeapYear(year): 
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    # Prompt the user to enter year and month 
    year = eval(input("Enter full year (e.g., 2001): "))
    month = eval(input(("Enter month as number between 1 and 12: ")))

    # Print calendar for the month of the year
    printMonth(year, month)
 
main()
'''



## 6.33 다각형 문제 구하기 [함수 사용]
'''
import math
def area(side):
    return 5 * math.pow(side, 2) / (4 * math.tan(math.pi/5))

def main():
    side = eval(input("Enter the side: "))
    print("The area of the polygon is " + str(area(side)))

main()
'''


## 6.34 -> 다각형 넓이 구하기 
#          공식 유도과정은 다시 봐야할 것. (적분 알아야함)
#          공식 : n * side * side / math.tan(math.pi / n) / 4 (이때, n은 n각형을 의미한다.)
'''
import math

def main():
    numberOfSides = eval(input("Enter the number of sides: "))
    side = eval(input("Enter the side: "))
    
    print("The area of the polygon is", area(numberOfSides, side))
  
def area(n, side):
    return n * side * side / math.tan(math.pi / n) / 4

main()
'''



## 6.35 -> 대문자 A 확률 구하기
'''
import RandomCharacter

N = 10000

count = 1
for i in range(N):
    if RandomCharacter.getRandomUpperCaseLetter() == 'A':
        count += 1

print("The probability of uppercase letter A is " + format(count / N * 100, "<5.2f") + "%")
'''


## 6.36 -> 신개념: 모듈 만든 뒤에 사용자 모듈 import 하는 방법!
#                 예전에 string으로 ascii 코드를 표현했지만 (문제 4.16 확인할 것!) 
#                 이 교재에서는 'A' to 'Z' 범위를 주고 표현하는 형식으로 코드 구현됨

import RandomCharacter

N = 100

count = 1
for i in range(N):
    if count % 10 == 0:
        print(RandomCharacter.getRandomUpperCaseLetter())
    else:
        print(RandomCharacter.getRandomUpperCaseLetter(), end = " ")
    count += 1
    
for i in range(N):
    if count % 10 == 0:
        print(RandomCharacter.getRandomDigitCharacter())
    else:
        print(RandomCharacter.getRandomDigitCharacter(), end = " ")
    count += 1
