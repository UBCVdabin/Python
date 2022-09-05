## Chapter 5에서 계속 봐야할 것들 (문제: )
## 질문 및 정답 확인 ()

## 5.1 
## 0이라는 숫자를 입력받기 전까지 최대값 최소값을 구한 뒤에 총합과 평균값 보여주기
#region 

#import sys

#positiveNumber = 0
#negativeNumber = 0
#total = 0
#count = 0
#number = -1

#while number != 0:
#    number = eval(input("Enter an integer, the input ends if it is 0: "))

#    if(count == 0 and number == 0):
#        print("You didn't enter any number")
#        sys.exit(0)

#    positiveNumber = number if number > positiveNumber else positiveNumber
#    negativeNumber = number if number < negativeNumber else negativeNumber
    
#    total += number
#    count += 1

#print("The number of positives is " + str(positiveNumber))
#print("The number of negatives is " + str(abs(negativeNumber)))
#print("The total is " + str(total))
#print("The average is " + str(round(total/count, 2)))

#endregion 




## 5.2 스피드 퀴즈 (뺄셈 문제)
'''
import random
import time

correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions
NUMBER_OF_QUESTIONS = 10 # Constant

startTime = time.time() # Get start time

while count < NUMBER_OF_QUESTIONS:
    # 1. Generate two random single-digit integers
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    # 2. If number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # 3. Prompt the student to answer "what is number1 - number2?" 
    answer = eval(input("What is " + str(number1) + " - " + 
        str(number2) + "? "))

    # 5. Grade the answer and display the result
    if number1 - number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong.\n", number1, "-",
            number2, "should be", (number1 - number2))

    # Increase the count
    count += 1

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correctCount, "out of", 
    NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")
'''



## 5.3 킬로그램, 파운드 동시에 찍기
#region
#print("Kilograms\tPounds")
#for i in range(1, 200, 2):
#    print(str(i) + "\t\t" + format(round(2.2 * i, 1), "5.1f"))
#endregion



## 5.4 마일과 킬로미터 동시에 찍기
#print("Miles\t\tKilometers")
#for i in range(1, 11):
#    print(str(i) + "\t\t" + format(round(1.609 * i, 3), "<6.3f"))



## 5.5 킬로그램 파운드 변환과정까지 포함하여 찍기
#region

#pounds = 20
#print("Kilograms\tPounds\t|  Pounds\tKilograms")
#print("--------------------------------------------------")
#for i in range(1, 200, 2):
#    print(str(i) + "\t\t" + format(round(2.2 * i, 1), "<6.1f"), end= "\t|  ")
#    print(str(pounds) + "\t\t" + format(round(pounds / 2.2, 2), "<6.2f"))
#    pounds += 5

#endregion



## 5.6 마일, 킬로미터 변환과정까지 포함하여 찍기
#region

#print(format("Miles", "<15s"), format("Kilometers", "10s"), 
#      "       |      ", format("Kilometers", "<15s"), format("Miles", "10s"))
#print("-----------------------------------------------------------------")

#miles = 1
#kilometers = 20
#count = 1
#while count <= 10:
#    print(format(miles, "<15d"), format(miles * 1.609, "<10.3f"), "       |      ", 
#          format(kilometers, "<15d"), format(kilometers / 1.609, "<10.3f"))
#    miles += 1
#    kilometers += 5
#    count += 1

#endregion



## 5.7 각도에 따른 sin, cos 값 보여주기
#region

#import math

#print("Degree\t\tSin\t\tCos")
#for i in range(0, 361, 10):
#    print(str(i) + "\t\t" + format(round(math.sin(math.radians(i)), 4), "<6.4f") + "\t\t" + format(round(math.cos(math.radians(i)), 4), "<6.4f"))

#endregion



## 5.8 0부터 20까지의 제곱근 값 보여주기
#region

#import math

#print("Number\t\tSquare Root")
#for i in range(0, 21, 2):
#    print(str(i) + "\t\t" + format(round(math.sqrt(i), 4), "<6.4f") + "\t\t")

#endregion



## 5.9 학비 증가 비용 구하기 (등비수열)
#region

#tuition = 10000   # Year 1
#total = 0
#rate = 1.05
#for years in range(10, 15):
#    if years == 10:
#        tuition = tuition * rate**years
#        total = tuition * rate**years
    
#    total = total * rate

#print("Tuition will be", tuition)
#print("Total cost will be", total)

#endregion



## 5.10 반학생이 몇 명인지 입력받은 다음 최고 점수 출력하기
#region

#numberofStudent = eval(input("Enter the number of student: "))

#highestScore = 0

#for i in range(0, numberofStudent):
#    score = eval(input("Enter the score which each student has gotten: "))
#    highestScore = score if score > highestScore else highestScore

#print("The highest score is " + str(highestScore))

#endregion



## 5.11 반학생이 몇 명인지 입력받은 다음 최고 점수와 그다음 높은 점수 함께 출력
#region

#numberofStudent = eval(input("Enter the number of student: "))

#highestScore = 0
#secondHighestScore = 0

#for i in range(0, numberofStudent):
#    score = eval(input("Enter the score which each student has gotten: "))
#    highestScore = score if score > highestScore else highestScore
#    secondHighestScore = score if score > secondHighestScore and highestScore > score else secondHighestScore

#print("The highest score is " + str(highestScore))
#print("The second highest score is " + str(secondHighestScore))

#endregion



## 5.12 100과 1000 사이에서 5와 6 약수가 포함하는 숫자 찍기
# 심플하지만 그래도 다시 봐야할 듯..
#region 

#count = 1
#for i in range(100, 1001):
#    if i % 5 == 0 and i % 6 == 0:
#        if count % 10 != 0:
#            print(i, end = " ")
#        else:
#            print(i)    
        
#        count += 1

#endregion


## 5.13 100과 200 사이에서 약수 5 또는 약수 6이 포함하는 숫자 찍기 (단, 둘다 포함하는 경우 제외)
#region

#count = 1
#for i in range(100, 200):
#    if i % 5 == 0 or i % 6 == 0 and not (i % 5 == 0 and i % 6 == 0):
#        if count % 10 != 0:
#            print(i, end = " ")
#        else:
#            print(i)    
        
#        count += 1
    
#endregion





## 5.14 제곱근 중 최대 숫자 뽑기
#region  

#number = 0
#while True:
#    if(number**2 > 12000):
#        break

#    number += 1

#print(number)

## 정답:
#i = 1

#while i * i <= 12000:
#    i += 1

#print("This number is", i)

#endregion





## 5.15 이번에는 세제곱근 찍기
#number = 0

#while (number + 1)**3 < 12000:
#    number += 1

#print(number)





## 5.16 보고 이해만! -> 문제 내용 해석이 잘 안됨
# 최대공약수 찾기 문제
'''

n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))

d = n1 if n1 < n2 else n2
while d >= 1:
    if n1 % d == 0 and n2 % d == 0:
        break
    d -= 1

print("GCD of", n1, "and", n2, "is", d)

'''



## 5.17 아스키 코드 찍기
'''
for i in range (0, 128):
    if i % 10 == 0:
        print(chr(i))
    else:
        print(chr(i), end = " ")

print()
'''



## 5.18 소수이면서 나누어지는 숫자 뽑아내기
#region 

#integer = eval(input("Enter an integer: "))

#divideNumber = 2

#while integer > 1:
#    if integer % divideNumber == 0:
#        if integer // divideNumber == 1:
#            print(divideNumber)
#        else:
#            print(divideNumber, end = ", ")

#        integer = integer // divideNumber
#        divideNumber = 2

#    else:
#        divideNumber += 1

#endregion



## 5.19 패턴 문제
#  1
# 212
#32123
#region

#lines = eval(input("Enter the number of lines: "))

#for i in range(1, lines + 1):
#    for j in range(i, lines):
#        print(end = "      ")
#    for j in range(i, 1, -1):
#        print(format(j, "<3d"), end = "   ")
#    print(1, end = "")
#    for j in range(2, i + 1):
#        print("   " + format(j, "3d"), end = "")
#    for j in range(lines, 1, -1):
#        print(end = "      ")
#    print()

#endregion



## 5.20 패턴 문제
#region

#def pattern(startIdx = 1, lastIdx = 0, isReverse = False, isSpace = False):
#    text = ""
    
#    steps = 1
#    if isReverse:
#        steps = -1
#    else:
#        lastIdx += 1

#    for i in range (startIdx, lastIdx, steps):
#        if(isSpace):
#            for j in range (i + 1, lastIdx):        # n - 1     // 5, 4, 3, 2, 1, 0
#                text += "  "
#        for j in range (0, i):                      # n         // 1, 2, 3, 4, 5, 6
#            text += str(j+1) + " "
        
#        text += "\n"


#    return text



#integer = eval(input("Enter an integer: "))


## pattern 1
#text = pattern(lastIdx = integer)
#print(text, end = "")


## pattern 2
#text = pattern(startIdx = integer, isReverse = True)
#print(text)


## pattern 3
#text = pattern(lastIdx = integer - 1)
#print(text, end = "")
#text = pattern(startIdx = integer, isReverse = True)
#print(text)

#endregion



## 5.21 패턴 + 제곱 문제
#region

#for i in range(1, 9):
#    for j in range(0, 8 - i):
#        print(end= "      ")
#    for j in range(0, i):
#        print(format(2**j, "6d"), end= "")
#    for j in range(i - 2, -1, -1):
#        print(format(2**j, "6d"), end= "")

#    print()

#endregion



## 5.22 2부터 1000까지 소수 찍기
#region 

#count = 0

#for i in range(2, 1001):
    
#    for j in range(2, i + 1):
#        if(i % j == 0):
#            if(j == i):
#                print(format(j, "5d"), end = "")
#                count += 1
#            else:
#                break;

#    if count == 8 and count % 8 == 0:
#        print()
#        count = 0

#endregion



## 5.23 대출 이자 문제
#region

#amount = eval(input("Loan Amount: "))
#years = eval(input("Number of Years: "))

#print("Interest Rate\t\tMonthly Payment\t\tTotal Paymant\n")

#rate = 5.000
#while True:
#    if rate > 8.000:
#        break


#    monthlyInterestRate = rate / 1200
#    monthlyPayment = amount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (years * 12))
#    totalPayment = monthlyPayment * years * 12

#    print(format(rate, "4.3f") + "%\t\t\t" + str(round(monthlyPayment, 2)) + "\t\t\t" + str(round(totalPayment, 2)))

#    rate += 0.125

#endregion



## 5.24 이자율 문제
#region 

#amount = eval(input("Loan Amount: "))
#years = eval(input("Number of Years: "))
#rate = eval(input("Annual Interest Rate: "))

#monthlyInterestRate = rate / 100 / 12



#monthlyPayment = amount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (years * 12))

#balance = amount
#print("Monthly Payment:", int(monthlyPayment * 100) / 100.0)
#print("Total Payment:", int(monthlyPayment * 12 * years * 100) / 100.0)


#print(format("Payment#", "<15s"), format("Interest", "<15s"), format("Principal", "<15s"), format("Balance", "<15s"))


#for i in range(1, years * 12 + 1):
#    interest = int(monthlyInterestRate * balance * 100) / 100.0
#    principal = int((monthlyPayment - interest) * 100) / 100.0
#    balance = int((balance - principal) * 100) / 100.0
#    print(format(i, "<15d"), format(interest, "<15.2f"), format(principal, "<15.2f"), format(balance, "<15.2f"))

#endregion





## 5.25 시리즈 문제 1 + 1/2 + 1/3
#sum = 0
#for i in range(1, 50001):
#    sum = sum + 1 / i

#print(sum)




## 5.26 시리즈 문제 1/3 + 3/5 + 5/7
#sum = 0
#for i in range (1, 98):
#    sum = sum + i / (i + 2)

#print(sum)





## 5.27 PI 공식 이용하여 보여주기
#region

#pi = 0
#item = 0

#for i in range(1, 100000 + 1):
#    item = (-1)**(i+1) / (2 * i - 1)
#    pi += item

#    if i == 10000 or i == 20000 or i == 30000 or i == 40000 or \
#          i == 50000 or i == 60000 or i == 70000 or i == 80000 or \
#          i == 90000 or i == 100000:
#        print("The PI is ", format(4 * pi, "16.15f"), " for i = ", i)

#endregion





## 5.28 나중에 다시 볼 것 팩토리얼의 개념과 시간 복잡도(?) -> factorial 함수로 만들어서 사용하는 것보다 훨씬 빠르다.
#region

#e = 1
#item = 1

#for i in range(1, 100000 + 1):
#    item = item / i     ## 원래는 1 / factorial 이 정상이다 하지만 연산할 때마다 처음부터 다시 팩토리얼을 구하기에
#                        ## 기존 값에 나누면 그게 팩토리얼이 된다. 
#                        ## 예를 들어 item 에 값이 1 이 있다고 가정한다.
#                        ## 그리고 i 는 2일 경우에 1 / 2 = 0.5가 된다. 이때 데이터는 사라지지 않는다.
#                        ## 따라서 0.5 인 상태에서 다시 3으로 나누면 이게 곧 팩토리얼이 된다.
#                        ## 0.5 -> 1/2          (1/2)/3 = 1/3!
#                        ## 따라서 item / i 는 팩토리얼로 사용한다.   
#    e += item

#    if i == 10000 or i == 20000 or i == 30000 or i == 40000 or \
#          i == 50000 or i == 60000 or i == 70000 or i == 80000 or \
#          i == 90000 or i == 100000:
#        print("The e is ", e, " for i = ", i)

#endregion





## 5.29 2001년부터 2101년까지의 윤년 찾아 프린팅 
#region 

#def CheckDayofMonth(month, leapYear = False):
#    if (month < 8 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
#        return 31
#    else:
#        if month == 2:
#            if leapYear:
#                return 29
#            else:
#                return 28
#        return 30

#count = 0

#for year in range(2001, 2101):
#    leapYear = False
    
#    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#        leapYear = True

#    if leapYear:
#        print(year, end= " ")
#        count += 1

#    if count % 10 == 0 and count != 0:
#        count = 0
#        print()

#print()

#endregion





## 5.30 zeller 공식 이용하여 해당 매달 첫번째 날짜 찾아 프린팅

## 참고: https://www.youtube.com/watch?v=T49yIEYc6uI
#region

#def monthofIntToString(month):
#    if month == 1:
#        return "January"
#    elif month == 2:
#        return "Febuaray"
#    elif month == 3:
#        return "March"
#    elif month == 4:
#        return "April"
#    elif month == 5:
#        return "May"
#    elif month == 6:
#        return "June"
#    elif month == 7:
#        return "July"
#    elif month == 8:
#        return "August"
#    elif month == 9:
#        return "September"
#    elif month == 10:
#        return "October"
#    elif month == 11:
#        return "November"
#    else:
#        return "December"

#def dayofIntToString(day):

#    if day == 0:
#        return "Sunday"
#    elif day == 1:
#        return "Monday"
#    elif day == 2:
#        return "Tuesday"
#    elif day == 3:
#        return "Wednesday"
#    elif day == 4:
#        return "Thursday"
#    elif day == 5:
#        return "Friday"
#    else:
#        return "Saturday"

#year = eval(input("Enter year: (e.g., 2008): "))


#j = 0
#k = 0
#for month in range(1, 13):
#    print(monthofIntToString(month) + " 1, " + str(year) + " is ", end = "")

#    if (month + 12) // 15 == 0:
#        j = (year - 1) // 100
#        k = (year - 1) % 100
#        month += 10
#    else:
#        j = year // 100
#        k = year % 100
#        month = (month + 12) % 15 + (month + 12) // 15 
 
#    dayoftheMonth = ( 1 + ((13 * month - 1) // 5) + k + (k//4) + (j//4) - 2 * j) % 7
#    print(dayofIntToString(dayoftheMonth))

#endregion



## 5.31 zeller 공식 달력 프린팅

#region

#def monthofIntToString(month):
#    if month == 1:
#        return "January"
#    elif month == 2:
#        return "Febuaray"
#    elif month == 3:
#        return "March"
#    elif month == 4:
#        return "April"
#    elif month == 5:
#        return "May"
#    elif month == 6:
#        return "June"
#    elif month == 7:
#        return "July"
#    elif month == 8:
#        return "August"
#    elif month == 9:
#        return "September"
#    elif month == 10:
#        return "October"
#    elif month == 11:
#        return "November"
#    else:
#        return "December"

#def dayofIntToString(day):

#    if day == 0:
#        return "Sunday"
#    elif day == 1:
#        return "Monday"
#    elif day == 2:
#        return "Tuesday"
#    elif day == 3:
#        return "Wednesday"
#    elif day == 4:
#        return "Thursday"
#    elif day == 5:
#        return "Friday"
#    else:
#        return "Saturday"
    
#def CheckDayofMonth(month, year):
#    leapYear = False
#    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#        leapYear = True

#    if (month < 8 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
#        return 31
#    else:
#        if month == 2:
#            if leapYear:
#                return 29
#            else:
#                return 28
#        return 30

#year = eval(input("Enter year: (e.g., 2008): "))

#print("")

#for month in range(1, 13):
#    j = 0
#    k = 0
#    days = CheckDayofMonth(month, year)

#    monthName = monthofIntToString(month) + " " + str(year)
#    print(monthName.center(40))
#    print("---------------------------------------")

#    for i in range(0, 7):
#        print(dayofIntToString(i)[0:3], end = "   ")
#    print()
    
    
#    if (month + 12) // 15 == 0:
#        j = (year - 1) // 100
#        k = (year - 1) % 100
#        month += 10
#    else:
#        j = year // 100
#        k = year % 100
#        month = (month + 12) % 15 + (month + 12) // 15 
 
#    startPoint = ( 1 + ((13 * month - 1) // 5) + k + (k//4) + (j//4) - 2 * j) % 7
    
  
    
#    for i in range(0, startPoint):
#        print("      ", end ="")

#    for i in range(1, days + 1):
#        if startPoint % 7 == 0 and startPoint == 7:
#            print()
#            startPoint = 1
#        else:
#            startPoint = startPoint + 1

#        print(format(i, "2d"), end = "    ")
#    print("\n")

#endregion



## 5.32 은행에다 적금 들기
#region
#amount = eval(input("Enter the monthly saving amount: "))
#annualRate = eval(input("Enter the annual interest rate: "))
#month = eval(input("Enter the number of months: "))

#monthlyRate = annualRate / 12 / 100
#monthlyRate = round(monthlyRate, 5)
#account = 0

#for i in range (0, month):
#    account = (amount + account) * ( 1 + monthlyRate )
#    account = round(account, 3)

#print("After the " + str(month) + " month, the account value is " + format(account, "<7.3f"))
#endregion



## 5.33 시간[기준: 월]별로 CD 가치 보여주기
#region
#amount = eval(input("Enter the initial deposit amount: "))
#annualRate = eval(input("Enter annual percentage yield: "))
#month = eval(input("Enter maturity period (number of months): "))
#CDValue = amount
#print("Month\tCD Value")
#for i in range (1, month + 1):
#    CDValue = CDValue + CDValue * annualRate / 1200
#    print(format(i, "<5d") + format(CDValue, "<7.2f"))
#endregion



## 5.34 로또 게임 
#  단 digit 1 != digit 2 달라야함
#region
import random

while True:
    lottery = random.randint(10, 99)

    lotterydigit1 = lottery // 10
    lotterydigit2 = lottery % 10
    if lotterydigit1 == lotterydigit2:
        break

    print("the lottery number is", lottery)
#endregion



## 5.35 퍼펙트 넘버 찾기 (예: 1 + 2 + 3 = 6) <= 1, 2, 3 은 소수!
# Question : How can I solve the problem as quickly as possible by using time complexity?
# 정답 :  i // 2 + 1 => 굳이 끝까지 탐색하면서 나눌 필요가 없다.
#region

#for i in range(1, 10000):
#    sum = 0
#    divisor = 1

#    for j in range(1, i // 2 + 1): 
#        if i % j == 0:
#            sum += j
#    if sum == i:
#        print(str(i) + " is perfect number.")

'''
    for j in range(i - 1, divisor, -1):
     if i % j == 0:
         sum += j
         sum += i // j
         divisor = divisor * (i // j)
         if divisor > j:
             break
'''
#endregion



## 5.36 가위, 바위, 보 게임 삼 세 판
#region
#import random

#standard = 0  # 2 -> user wins
#              # -2 -> computer wins

#while standard < 2 and standard > -2:

#    computer = random.randint(0, 2)
#    yourChoice = eval(input("scissor (0), rock (1), paper (2): "))
    
#    if computer == 0:
#        if yourChoice == 0:
#            print("The computer is scissor. You are scissor too. It is a draw.")

#        elif yourChoice == 1:
#            print("The computer is scissor. You are rock. You win")
#            standard += 1

#        else:
#            print("The computer is scissor. You are paper. You lost")
#            standard -= 1
    
#    if computer == 1:
#        if yourChoice == 0:
#            print("The computer is rock. You are scissor. You lost.")
#            standard -= 1

#        elif yourChoice == 1:
#            print("The computer is rock. You are rock too. It is a draw. ")

#        else:
#            print("The computer is rock. You are paper. You won.")
#            standard += 1
    
#    if computer == 2:
#        if yourChoice == 0:
#            print("The computer is paper. You are scissor. You won.")
#            standard += 1

#        elif yourChoice == 1:
#            print("The computer is paper. You are rock. You lost.")
#            standard -= 1

#        else:
#            print("The computer is paper. You are paper too. It is a draw.")
#endregion



## 5.37 시리즈 문제 
#region

#import math
#sum = 0
#for i in range (1, 624):
#    sum += 1 / ( math.sqrt(i) + math.sqrt(i+1))

#print(sum)

#endregion



## 5.38 카운트 다운 (time.sleep)
#region

#import time
#seconds = eval(input("Enter the number of seconds: "))

#time.sleep(1)
#for i in range(seconds - 1, 0, -1):
#    print(str(i) + " seconds remaining" if i > 1 else str(i) + " second remaining")
#    time.sleep(1)

#print("Stopped")

#endregion



## 5.39
#region

def GetCommission(salesAmount):
    if salesAmount >= 0 and salesAmount <= 5000:
        return  salesAmount * 0.08
    elif salesAmount > 5000 and salesAmount <= 10000:
        # return 5000 * 0.08 + (salesAmount - 5000) * 0.10
        return salesAmount * 0.10
    else:
        # return 5000 * 0.08 + 5000 * 0.10 + (salesAmount - 10000) * 0.12
        return salesAmount * 0.12
def main():
    baseSalary = 5000
    targetSalary = int(input("Enter target salary"))
    targetCommission = targetSalary - baseSalary

    salesAmount = 0
    commission = 0
    while commission < targetCommission:

        salesAmount += 1

        commission = GetCommission(salesAmount)

        

    print(salesAmount)

main()


#endregion



## 5.40
#region

#import random

#print("Does the coin display the head or tail?[i.g 0(=head), 1(=tail)]")
#input("In order to look at the coin, please press an enter key.")

#for i in range (0, 1000000): 
#    coin = random.randint(0,1)
#    print(coin)

#endregion



## 5.41
'''
number = eval(input("Enter a number (0: for end of input): "))
count = 1 
largestNumber = number
while number != 0:
    number = eval(input("Enter a number (0: for end of input): "))

    if number == largestNumber:
        count += 1

    if number > largestNumber:
        largestNumber = number
        count = 1
  


print("The largest number is " + str(largestNumber))
print("The occurrence count of the largest number is " + str(count))
'''



## 5.42 Question I don't know the Monte Carlo rule.. # 해결함 !
#region 

#import random
#import math

#def GetRandomCoordinate():
#    x = random.randint(-100, 100)
#    x /= 100
#    return x

#def GetPointLocation(x, y):
#    y_Max = 1 - x          #=> y= ax + b

#    if(y < y_Max or DblEquals(y, y_Max)):
#        return 1
#    else:
#        return 0


#def DblEquals(val1, val2, epsilon = 0.000001):
#    if abs(val1 - val2) < epsilon:
#        return True
#    else:
#        return False

#numberOfHits = 0
#numberOfTries = 5000

#for i in range(numberOfTries):
#    pointX = GetRandomCoordinate()
#    pointY = GetRandomCoordinate()
    
#    if pointX < 0:
#        numberOfHits += 1

#    else:
#        if not (pointX > 1 or pointX < 0 or pointY > 1 or pointY < 0):
#            numberOfHits += GetPointLocation(pointX, pointY)

#print(numberOfHits)
#print("The probability in Region 1 and 3 is",
#    1.0 * numberOfHits / numberOfTries)

#endregion


## 5.43
'''
import random

for i in range(1, 8):
    for j in range(1, 8):
        print(i, j)

number = str(random.randint(1, 7)) + str(random.randint(1, 7))

print("The total number of all combinations is " + number)
'''



## 5.44
#region

#decimal = eval(input("Enter an integer: "))
    
#binaryString = ""
#value = decimal

#while value != 0:
#    binaryString = str(value % 2) + binaryString
#    value = value // 2

#print(str(decimal) + "'s binary representation is " + binaryString)

#endregion



## 5.45
'''
def changeHex(value):
    value = value % 16

    if value == 10:
        return "A"
    elif value == 11:
        return "B"
    elif value == 12:
        return "C"
    elif value == 13:
        return "D"
    elif value == 14:
        return "E"
    elif value == 15:
        return "F"
    else:
        return str(value)

decimal = eval(input("Enter an integer: "))
    
HexString = ""
value = decimal

while value != 0:
    HexString = changeHex(value) + HexString
    value = value // 16

print(str(decimal) + "'s Hexcode representation is " + HexString)
'''



## 5.46
'''
number = eval(input("Enter ten numbers: "))
sum = number
pow = number**2
for i in range(1, 10):

    number = eval(input())
    sum += number
    pow += number**2

mean = sum / 10
deviation = (( pow - sum**2 / 10 ) / 9)**0.5 

print("The mean is " + format(mean, "3.2f"))
print("The standard deviation is " + format(deviation, "6.5f"))
'''


