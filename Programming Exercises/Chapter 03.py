## Chapter 3에서 계속 봐야할 것들 (문제: 3.2, 3.8[정답])

## 3.1 오각형 넓이 구하기
'''
import math
radius = eval(input("Enter the length from the center to a vertex: "))
s = 2 * radius * math.sin(math.pi /5)
area = 3 * math.sqrt(3) / 2 * math.pow(s,2)

print("The area of the pentagon is " + str(round(area, 2)))
'''



## 3.2 구의 두점 사이 거리 구하기 공식좀 볼 것... (※ in degrees : 각도 값으로 받았으니, radian으로 바꿔야 한다.)                                                                   
'''
import math
RADIUS = 6371.01
latitude_1, longitude_1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))      
latitude_2, longitude_2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

d = RADIUS * math.acos(math.sin(math.radians(latitude_1)) * math.sin(math.radians(latitude_2)) + math.cos(math.radians(latitude_1)) *\
                       math.cos(math.radians(latitude_2)) * math.cos(math.radians(longitude_1)- math.radians(longitude_2)))

print("The distance between the two points is " + str(d))
'''




## 3.4 math.pi = 라디안이다. 즉, 180도를 라디안으로 하면 Pi가 나옴 [=> print(math.radians(180)) == print(math.pi)]
'''
import math
side = eval(input("Enter the side: "))
area = 5 * math.pow(side, 2) / (4 * math.tan(math.pi/5))
print("The area of the pentagon is " + str(area))
'''




## 3.5 다각형 넓이 구하기
'''
import math
count = eval(input("Enter the number of sides: "))
side = eval(input("Enter the side: "))

area = count * side**2 / (4 * math.tan(math.pi / count))
print("The area of the polygon is " + str(area))
'''




## 3.6 숫자를 입력받아 ASCII code 보기
'''
import sys
code = eval(input("Enter an ASCII code: "))

if code > 127 or code < 0:
    print("The number of the code does not exist..")
    sys.exit(0)

code = chr(code)

print("The character is " + code)
'''



## 3.7 난수를 이용해 문자 찍기
'''
import time
char = chr(int(time.time() % 127))
print(char)
'''




## 3.8 내 버전 [금액 상세하게 보여주기]
'''
amount = eval(input("Enter an amount, for example, 1156: "))

numberOfOneDollars = amount // 100
numberOfOneCents = amount % 100

print("Your amount " + str(amount) + " consists of\n"\
    + str(numberOfOneDollars) + " dollars\n"\
    + str(numberOfOneCents) + " cents")
'''

## 3.8 정답
'''
# Receive the amount 
amount = eval(input("Enter an amount as integer, e.g., 1156 for 11 dollars 56 cents: "))

# Convert the amount to cents
remainingAmount = amount

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display results
print("Your amount " + str(amount) + " consists of \n" + 
      "\t" + str(numberOfOneDollars) + " dollars\n" + 
      "\t" + str(numberOfQuarters) + " quarters\n" +
      "\t" + str(numberOfDimes) +  " dimes\n" + 
      "\t" + str(numberOfNickels) + " nickels\n" +
      "\t" + str(numberOfPennies) + " pennies")
'''




## 3.9 직원 월급
'''
name = input("Enter employee\'s name: ")
hour = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: "))
federal_taxrate = eval(input("Enter federal tax withholding rate: "))
state_taxrate = eval(input("Enter state tax withholding rate: "))

gross_pay = rate * hour
federal_tax = round(gross_pay * federal_taxrate, 2)
state_tax = round(gross_pay * state_taxrate, 2)

print("\nEmployee Name: " + str(name))
print("Hours Worked: " + str(hour))
print("Pay Rate: $" + str(rate))
print("Gross Pay: $" + str(gross_pay))
print("Deductions:")
print("\tFederal Withholding (" + str(federal_taxrate) + "%): $" + str(federal_tax))
print("\tState Withholding (" + str(federal_taxrate) + "%): $" + str(state_tax))
print("\tTotal Deduction:  $" + str(federal_tax + state_tax))
print("Net Pay: $" + str(gross_pay - (federal_tax + state_tax)))
'''