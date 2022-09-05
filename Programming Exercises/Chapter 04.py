## Chapter 4에서 계속 봐야할 것들 (문제: 4.11, 4.32, 4.34)
## 질문 및 정답 확인 (4.3, 4.5, 4.7, 4.9, 4.11, 4.15)

## 4.1
'''
import math
a,b,c = eval(input("Enter a, b, c: "))
if b**2 - 4 * a * c > 0:
    root_a = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    root_b = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    print("The roots are " + str(root_a) + " and " + str(root_b))
elif b**2 - 4 * a * c == 0:
    root = -b / (2 * a)
    print("The roots is " + str(root))
else:
    print("The equation has no real roots")
'''




## 4.2
'''
import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)

yourAnswer = eval(input("What is "+ str(number1) + " + " + str(number2) + " + " + str(number3) + " ? "))

print(str(number1) + " + " + str(number2) + " + " + str(number3) + " = " + str(yourAnswer) + " is " + str(yourAnswer == number1 + number2 + number3))
'''




## 4.3
'''
import sys

a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

if a * d == b * c:
    print("The equation has no solution")
    sys.exit(0)

x = (d * e - b * f) / (a * d - b * c)
y = (a * f - c * e) / (a * d - b * c)

print("x is", x, "and y is", y)
'''



## 4.4
'''
import random

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

answer = eval(input("What is " + str(number1) +" + " + str(number2) + " ? "))

if number1 + number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n" + str(number1), '+', number2, "is", number1 + number2, '.')
'''



## 4.5 람다 표현식 활용 
'''
def dayNumberToString(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuseday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    else:
        return "Saturday"

day = eval(input("Enter today's day: "))
 

numberOfDay = eval(input("Enter the number of days elapsed since today: "))
futureday = day + numberOfDay % 7
futureday = futureday % 7
print("Today is", dayNumberToString(day), "and the future day is", dayNumberToString(futureday))


## Check Date

#--------------------------------------------------------------------------------------------------------
#dateCheck = 
##if numberOfDay < day:
##    dateCheck = 1
##elif numberOfDay > day:
##    dateCheck = 2
##else:
##    dateCheck = 0

#day = day % 6

#if dateCheck == 1:
#    print("Today is", dayNumberToString(day), "and the past day is", dayNumberToString(futureday))
#elif dateCheck == 2:
#    print("Today is", dayNumberToString(day), "and the future day is", dayNumberToString(futureday))
#else:
#    print("Today is", dayNumberToString(day))
#---------------------------------------------------------------------------------------------------------
 '''



## 4.6 단위 변환 (pounds to kilograms)
'''
pounds = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))

kilograms = pounds * 0.45359237                     # ratio from pounds to kilograms : 0.45359237
inches = inches + 12 * feet
height = inches * 0.0254

BMI = kilograms / height / height                   # weight(kg) / height / height (m)
print("BMI is " + str(BMI))

if BMI < 18.5:
    print("You are Underweight !")
elif BMI < 25:
    print("You are Normal !")
elif BMI < 30:
    print("You are Overweight !")
else:
    print("You are obese !")
'''



## 4.7
'''
# Receive the amount 
amount = eval(input("Enter an amount as integer, e.g., 1156 for 11 dollars 56 cents: "))
result = "Your amount " + str(amount) + " consists of \n"

# Convert the amount to cents
remainingAmount = amount

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

result += "\t" + str(numberOfOneDollars) + " dollars\n" if numberOfOneDollars > 0 else "" 

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

result += "\t" + str(numberOfQuarters) + " quarters\n" if numberOfQuarters > 0 else "" 

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

result += "\t" + str(numberOfDimes) + " dimes\n" if numberOfDimes > 0 else "" 

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

result += "\t" + str(numberOfNickels) + " nickels\n" if numberOfNickels > 0 else "" 

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

result += "\t" + str(numberOfPennies) + " pennies\n" if numberOfPennies > 0 else "" 

# Display results
print(result)
'''



## 4.8 ask teacher to use this if statements.
'''
number1, number2, number3 = eval(input("Enter numbers : "))
if number1 > number2:
    number1, number2 = number2, number1
if number1 > number3:
    number1, number3 = number3, number1
if number2 > number3:
    number2, number3 = number3, number2

print("Increasing Order :", number1, "<", number2, "<", number3)
'''




## 4.9
'''
weight_1, price_1 = eval(input("Enter weight and price for package 1: "))
weight_2, price_2 = eval(input("Enter weight and price for package 2: "))

pricePerWeightForPackage_1 = price_1 / weight_1
pricePerWeightForPackage_2 = price_2 / weight_2

if pricePerWeightForPackage_1 > pricePerWeightForPackage_2:
    print("Package 1 has the better price")
elif pricePerWeightForPackage_1 < pricePerWeightForPackage_2:
    print("Package 2 has the better price")
else:
    print("Both are the same price")
'''




## 4.10
'''
import random

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input("What is " + str(number1) +" - " + str(number2) + " ? "))

if number1 - number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", number1, '-', number2, "is", number1 - number2, '.')
'''




## 4.11 달력 윤달 계산
'''
import sys
def CheckDayofMonth(month, leapYear = False):
    if (month < 8 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
        return 31
    else:
        if month == 2:
            if leapYear:
                return 29
            else:
                return 28
        return 30

def monthofIntToString(month):
    if month == 1:
        return "January"
    elif month == 2:
        return "Febuaray"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    else:
        return "December"

month, year = eval(input("Enter month, year: "))


if year < 0 or month < 0 or month > 12:
    print("Invalid Date")
    sys.exit(0)

leapYear = False

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    leapYear = True

print(monthofIntToString(month) + " " + year + " has "+ CheckDayofMonth(month, leapYear) + " days")
'''




## 4.12
'''
number = eval(input("Enter an integer: "))
print("Is", number, "divisible by 5 and 6?", (number % 5 == 0 and number % 6 == 0))
print("Is", number, "divisible by 5 or 6?", (number % 5 == 0 or number % 6 == 0))
print("Is", number, "divisible by 5 or 6?, but not both?", (number % 5 == 0 or number % 6 == 0 and not number % 5 == 0 and number % 6 == 0))
'''






## 4.13 Tax 계산
'''
import sys

# Prompt the user to enter filing status
status = eval(input(
    "(0-single filer, 1-married jointly,\n" +
    "2-married separately, 3-head of household)\n" +
    "Enter the filing status: "))

# Prompt the user to enter taxable income
income = eval(input("Enter the taxable income: "))

# Compute tax
tax = 0

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
              (372950 - 171550) * 0.33 + (income - 372950) * 0.35;

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
              (372950 - 208850) * 0.33 + (income - 372950) * 0.35;

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
              (186475 - 104425) * 0.33 + (income - 186475) * 0.35;


elif status == 3: # Compute tax for head of household
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
              (372950 - 190200) * 0.33 + (income - 372950) * 0.35;
else:
    print("Error: invalid status")
    sys.exit()

# Display the result
print("Tax is", format(tax, ".2f"))
'''






## 4.14
'''
import random

coin = random.randint(0,1)

userGuess = eval(input("Does the coin display the head or tail?\n Enter your guess [i.g 0(=head), 1(=tail)] :"))

if (coin == userGuess):
    print("You are correct!")
else:
    print("You are wrong..")
'''





## 4.15 반복문, 함수
'''
import random

def SeperateDigit(number):
    digit = []

    while True:
        if number == 0:
            digit.reverse()
            return digit

        digit.append(number % 10)

        number = number // 10

def SeperateDigit_1(number):
    SeperateFirstDigit = number // 100
    SeperateSecondDigit = ( number % 100 ) // 10
    SeperateThirdDigit = number % 10 

    return SeperateFirstDigit, SeperateSecondDigit, SeperateThirdDigit


#lottery = random.randint(100, 999)

lottery = 123
d1, d2, d3 = SeperateDigit_1(lottery)


guess = eval(input("Enter your lottery pick (three digits): "))
g1, g2, g3 = SeperateDigit_1(guess)

print("The lottery number is", lottery)

if guess == lottery:
    print("Exact match: you win $10,000")

else:
    if (d1 == g1 or d1 == g2 or d1 == g3) and (d2 == g1 or d2 == g2 or d2 == g3) and (d3 == g1 or d3 == g2 or d3 == g3):
        print("Match all digits: you win $3,000")
    elif d1 == g1 or d1 == g2 or d1 == g3 or d2 == g1 or d2 == g2 or d2 == g3 or d3 == g1 or d3 == g2 or d3 == g3:
        print("Match one digit: you win $1,000")
    else:
        print("Sorry, no match")



#else:
#    #lotteryDigit = SeperateDigit(lottery)
#    #guessDigit = SeperateDigit(guess)
    
#    #count = 0
    
#    #for lottery_Digit in lotteryDigit:
#    #    for guess_Digit in guessDigit:
#    #        if(lottery_Digit == guess_Digit):
#    #            count = count + 1
    
#    #if count == 3:
#    #    print("Match all digits: you win $3,000")
#    #elif count > 0:
#    #    print("Match one digit: you win $1,000")
#    #else:        
#    #    print("Sorry, no match")
'''





## 4.16 임시 비밀번호 만들 때 유용한 코드
'''
import random
import string

ch = random.choice(string.ascii_uppercase)      # Method 1
print(ch)
print(chr(random.randint(ord('A'), ord('Z'))))  # Method 2
'''





## 4.17
'''
import random

computer = random.randint(0, 2)
yourChoice = eval(input("scissor (0), rock (1), paper (2): "))

if computer == 0:
    if yourChoice == 0:
        print("The computer is scissor. You are scissor too. It is a draw.")
    elif yourChoice == 1:
        print("The computer is scissor. You are rock. You win")
    else:
        print("The computer is scissor. You are paper. You lost")

if computer == 1:
    if yourChoice == 0:
        print("The computer is rock. You are scissor. You lost.")
    elif yourChoice == 1:
        print("The computer is rock. You are rock too. It is a draw. ")
    else:
        print("The computer is rock. You are paper. You won.")

if computer == 2:
    if yourChoice == 0:
        print("The computer is paper. You are scissor. You won.")
    elif yourChoice == 1:
        print("The computer is paper. You are rock. You lost.")
    else:
        print("The computer is paper. You are paper too. It is a draw.")
'''





## 4.18
'''
RMB = eval(input("Enter the exchange rate from dollars to RMB: "))
covertMode = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))


if covertMode == 0:
    amount = eval(input("Enter the dollar amount: "))
    exchange = amount * RMB
    print(amount, "is", exchange, "yuan")
else:
    amount = eval(input("Enter the RMB amount: "))
    exchange = amount / RMB
    print(amount, "is", round(exchange, 2), "dollar")
'''





## 4.19
'''
a, b, c = eval(input("Enter three edges: "))

if a < b:
    a, b = b, a

if a < c:
    a, c = c, a

if a < b + c:
    print("The perimeter is " + str(a+b+c))
else:
    print("The input is invalid")
'''






## 4.20
'''
import sys

# Enter the temperature in Fahrenheit
fahrenheit = eval(input("Enter the temperature in Fahrenheit: ")) 

if fahrenheit < -58 or fahrenheit > 41:
    print("Temperature must be between -58F and 41F")
    sys.exit()

# Enter the wind speed miles per hour
speed = eval(input("Enter the wind speed miles per hour: "))
    
if speed < 2:
    print("Speed must be greater than or equal to 2")
    sys.exit()

# Compute wind chill index
windChillIndex = 35.74 + 0.6215 * fahrenheit - 35.75 * \
      speed ** 0.16 + 0.4275 * fahrenheit * speed ** 0.16
      
# Display the result
print("The wind chill index is", windChillIndex)
'''




## 4.21 00년도 달력 날짜 요일 파악하기

def dayofIntToString(day):
    if day == 0:
        return "Saturday"
    elif day == 1:
        return "Sunday"
    elif day == 2:
        return "Monday"
    elif day == 3:
        return "Tuesday"
    elif day == 4:
        return "Wednesday"
    elif day == 5:
        return "Thursday"
    else:
        return "Friday"


year = eval(input("Enter year: (e.g., 2008): "))
month = eval(input("Enter month: 1-12: "))
day = eval(input("Enter the day of the month: 1-31: "))

leapYear = False 
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    leapYear = True


if month == 1 or month == 2:
    month += 12
    j = ( year - 1) // 100 
    k = ( year - 1) % 100
else:
    j = year // 100 
    k = year % 100


dayoftheMonth = ( day + (26 * (month + 1) // 10) + k + (k // 4) + (j // 4) + 5*j ) % 7
dayoftheMonth = int(dayoftheMonth)
print("Day of the week is " + dayofIntToString(dayoftheMonth))





## 4.22

#import math

#def getPointFromUser(prompt):
#    x, y = eval(input(prompt))
#    return x, y

#def dist(x, y):
#    return math.sqrt(math.pow(x,2) + math.pow(y,2))

#def checkDistance(dist, radius):
#    if dist <= radius:
#        return True
#    else:
#        return False

#def printResult(x, y, isInCircle):
#    if isInCircle:
#        print("Point (" + str(float(x)) + ", " + str(float(y)) + ") is in the circle")
#    else:
#        print("Point (" + str(float(x)) + ", " + str(float(y)) + ") is not in the circle")

#x, y = getPointFromUser("Enter a point with two coordinates: ")

#distance = dist(x, y)
#result = checkDistance(distance, 10)
#printResult(x, y, result)






## 4.23
'''
import sys

x, y = eval(input("Enter a point with two coordinates: "))

if(abs(x) > 5 or abs(y) > 2.5):
    print("Point (" + str(float(x)) + ", " + str(float(y)) + ") is not in the rectangle")
    sys.exit(0)

print("Point (" + str(float(x)) + ", " + str(float(y)) + ") is in the rectangle")
'''




## 4.24
'''
import random

def rankOfCard(number):
    result = ""
    number = number % 13

    if number == 1:
        result = "Ace"
    elif number == 11:
        result = "Jack"
    elif number == 12:
        result = "Queen"
    elif number == 13:
        result = "King"
    else:
        result = str(number)

    return result

def suitofCard(number):
    if number // 13 == 0:
        result = "Clubs"
    elif number // 13 == 1:
        result = "Diamonds"
    elif number // 13 == 2:
        result = "Hearts"
    else:
        result = "Spades"

    return result

rank = random.randint(1, 52)
rank = random.randint(1, 4)
print(rank)

print("The card you picked is the", rankOfCard(rank), "of", suitofCard(rank))
'''




## 4.25
'''
x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4: "))

a = (y1 - y2)
b = -(x1 - x2)
c = (y3 - y4)
d = -(x3 - x4)

e = ((y1 - y2) * x1 - (x1 - x2) * y1)
f = ((y3 - y4) * x3 - (x3 - x4) * y3)


Slope = b*c - a*d



if Slope == 0:
    if  e == f:
        print("The two lines are the same")
    else:
        print("The two lines are parallel")
else:
     print("The intersecting point is at (" + str(( d * e - b * f ) / (a * d - b * c )) + ", " + str(( a * f - e * c ) / ( a * d - b * c )) +")")
'''




## 4.26 숫자 되돌림
'''
number = eval(input("Enter a three-digit integer: "))

tempNumber = number
palindrome = 0 

while(True):
    if(tempNumber == 0):
        break

    palindrome *= 10
    palindrome += tempNumber % 10
    tempNumber //= 10

if(number == palindrome):
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")
'''




## 4.27 삼각형과 점 거리
'''
x, y = eval(input("Enter a point's x- and y-coordinates: "))

y1 = ((-1/2) * x) + 100

if((x >= 0 and x <= 200) and (y >= 0 and y <= 100) and y <= y1):
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")
'''




## 4.28 조건문 다시 볼 것..
'''
x_1, y_1, width_1, height_1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
x_2, y_2, width_2, height_2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))


if((x_1 - width_1 / 2) <= x_2 and (x_1 + width_1 / 2) >= x_2 or (y_1 - height_1 / 2) <= y_2 and (y_1 + height_1 / 2) >= y_2):
    if((x_1 - width_1 / 2) <= (x_2 - width_2 / 2) and (x_1 + width_1 / 2) >= (x_2 + width_2 / 2) and (y_1 - height_1 / 2) <= (y_2 - height_2 / 2) and (y_1 + height_1 / 2) >= (y_2 + height_2 / 2)):
        print("r2 is inside r1")
    else:
        print("r2 overlaps r1")

else:
    print("r2 does not overlap r1")



## 밑에 예제도 같이 볼 것.
x1, y1, w1, h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))

x2, y2, w2, h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

xDistance = x1 - x2 if x1 - x2 >= 0 else x2 - x1
yDistance = y1 - y2 if y1 - y2 >= 0 else y2 - y1
    
if xDistance <= (w1 - w2) / 2 and yDistance <= (h1 - h2) / 2:
    print("r2 is inside r1")
elif xDistance <= (w1 + w2) / 2 and yDistance <= (h1 + h2) / 2:
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")
'''




## 4.29 원 거리 관계 (두 점 사이 거리와 반지름으로 구함)
'''
import math
x1, y1, radius1 = eval(input("Enter circle's center x-, y-coordinates, and radius: "))
x2, y2, radius2 = eval(input("Enter circle's center x-, y-coordinates, and radius: "))


distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    
if  radius1 >= (distance + radius2):
    print("circle2 is inside circle1")
elif  radius1 > (distance - radius2):
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")
'''




## 4.30
'''
import time

GMT = eval(input("Enter the time zone offset to GMT: "))

currentTime = time.time()

totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60			## 60초

totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60			## 60분

totalHours = totalMinutes // 60
currentHours = totalHours % 24				## 24시간
currentHours = (currentHours + GMT) % 24    ## 현재 시간

AM_PM = "AM" if currentHours >= 0 and currentHours < 12 else "PM"

print("Current time is " + str(currentHours).zfill(2) + ":" + str(currentMinutes).zfill(2) + ":" + \
		str(currentSeconds).zfill(2) + " " + AM_PM)		                                                 	        ## zfill 함수는 숫자 여백에 0을 채워넣어주는 함수이다. 
																													## 뒤의 매개변수는 얼마만큼 넣어줄 수 있는지 명시적으로 기재해줘야 한다.

#print("12".zfill(2))																								## [결과: 12], 그리고 변수 아닌 리터널 상수에 함수에 이용 가능! (파이썬의 특징 1) 
#print("6".zfill(2))	
'''




## 4.31 선과 점 사이의 관계
'''
x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

if(x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0:
    print("p2 is on the same line from p0 to p1")
elif (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) > 0:
    print("p2 is on the left side of the line from p0 to p1")
else:
    print("p2 is on the right side of the line from p0 to p1")
'''




## 4.32
'''
x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))

if(x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0 and abs(x1 - x0) >= x2 and abs(y1 - y0) >= y2:
    print("(" + str(x2) + ", " + str(y2) + ")", "is on the line segment from (" + str(x0) + ", " + str(y0) + ") to (" + str(x1) + ", " + str(y1) + ")")
else:
    print("(" + str(x2) + ", " + str(y2) + ")", "is not on the line segment from (" + str(x0) + ", " + str(y0) + ") to (" + str(x1) + ", " + str(y1) + ")")


## 정답 코드 
x0, y0, x1, y1, x2, y2 = eval(input("Enter three points for p0, p1, and p2: "))

status = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    
if status <= 0.0000000001 and \
        ((x0 <= x2 and x2 <= x1) or (x0 >= x2 and x2 >= x1)):
    print("(" + str(x2) + ", " + str(y2) + ") is on the line segment from"
        + " (" + str(x0) + ", " + str(y0) + ") to " + "(" + 
        str(x1) + ", " + str(y1) + ")")
else: 
    print("(" + str(x2) + ", " + str(y2) + ") is not on the line segment from"
        + " (" + str(x0) + ", " + str(y0) + ") to " + "(" 
        + str(x1) + ", " + str(y1) + ")")
'''





## 4.33
'''
decimal = eval(input("Enter a decimal value (0 to 15): "))

if decimal >= 0 and decimal <= 9:
    print("The hex value is" , decimal)
elif decimal <= 15 and decimal >= 10:
    print("The hex value is", chr(decimal + 55))
else: 
    print("Invalid input")
'''





## 4.34 다시 볼것
'''
hexChar = input("Enter a hexChar character: ").strip()

if hexChar >= '0' and hexChar <= '9':
    print("The decimal value is" , ord(hexChar) - ord('0'))
elif hexChar <= 'F' and hexChar >= 'A':
    print("The decimal value is", ord(hexChar) - ord('A') + 10)
elif hexChar <= 'f' and hexChar >= 'a':
    print("The decimal value is", ord(hexChar) - ord('a') + 10)
else: 
    print("Invalid input")
'''