
## Chapter 2에서 계속 봐야할 것들 (문제: 2.6, 2.14, 2.18)
import Common.Util as util



## 2.1 썹씨를 화씨로 변환
'''
celsius = eval(input("Enter a degree in Celsius: "))
print(str(celsius) + " Celsius is " + str((9 / 5) * celsius + 32) + " Fahrenheit")
'''




## 2.2 원의 넓이와 원기둥 부피 구하기
'''
import math

#radius, length = eval(input("Enter the radius and length of a cylinder :"))			# eval 은 문자열을 숫자로 변경해주는 함수이다. 
																						# 단, 3a, b 같은 혼합문자는 인식하지 못한다. 
																						# 또한, 특수기호 관련해서, ' '(스페이스 또는 여백)는 공백을 제거해주는 역할만 하며, 
																						# ','(쉼표) 문자 만 split separator로 인식하여 숫자를 구분짓게 도와준다.

#radius, length = input("Enter the radius and length of a cylinder :").split(',')		# split 작은 따옴표만 구분자로 사용한다. 
																						# 위에 Statement 문과 마찬가지로 여백은 기본적으로 제거해준 상태로 ','를 split 한다.


radius = float(radius)
length = float(length)

area = radius * radius * math.pi
volume = area * length

print("The area is", round(area, 4))
print("The volume is", round(volume, 1))
'''




## 2.3 feet 을 미터로 변환
'''
feet = eval(input("Enter a value for feet: "))
print(str(feet) + " feet is " + str(round(feet * 0.305, 4)) + " meters")
'''





## 2.4 pound 를 kilogram으로 변환
'''
pound = eval(input("Enter a valus in pounds: "))
print(pound, "pounds is", round(pound * 0.454, 3), "kilograms")
'''





## 2.5 기여금 계산 및 받을 총액 구하기
'''
subtotal, rate = eval(input("Enter the subtotal and a gratuity rate: "))
gratuity =  round(subtotal * (rate / 100), 2);
print("The gratuity is " + str(gratuity) + " and the total is " + str(subtotal + gratuity))
'''





## 2.6 -> 중요 ! 각 숫자 자리 더하기 (예: 1234 => 1+2+3+4 = 10)
'''

number = eval(input("Enter a number between 0 and 1000: "))
if (number >=0 and number <= 1000):
	sum = 0
	while number > 0:
		sum += number % 10
		number //= 10

print("The sum of the digits is", sum)

'''





## 2.7 사용자에게 시간(분 단위)를 입력 받아 날짜 찍기
'''
minutes = eval(input("Enter the number of minutes: "))
wholeDays = minutes // 60 // 24
years =  wholeDays // 365;
days = wholeDays % 365
print(str(minutes) + " minutes is approximately " + str(years) + " years and " + str(days) + " days")
'''





## 2.8 열 에너지(?) 구하는 공식
'''

massinKilograms = eval(input("Enter the amount of water in kilograms: "))
initialTemperature = eval(input("Enter the initial temperature: "))
finalTemperature = eval(input("Enter the final temperature: "))

quantity = massinKilograms * (finalTemperature - initialTemperature) * 4184

print("The energy needed is", round(quantity, 1))

'''






## 2.9 화씨 온도와 속력을 입력 받아 바람의 온도와 세기를 출력함
'''
fahrenheit = eval(input("Enter the temperature is Fahrenheit between -58 and 41: "))
speed = eval(input("Enter the wind speed in miles per hour: "))
windChill = 35.74 + 0.6215 * fahrenheit - 35.75 * speed**0.16 + 0.4275 * fahrenheit * speed**0.16
print("The wind Chill index is " + str(round(windChill, 5)))
'''





## 2.10
'''
speed, acceleration = eval(input("Enter speed and acceleration: "))

length = speed**2 / (2 * acceleration)

print("The minimum runway length for this airplane is", round(length, 3), "meters")
'''





## 2.11
'''
finalAccount = eval(input("Enter final account value: "))
rate = eval(input("Enter annual interest rate in percent: "))
years = eval(input("Enter number of years: "))

initialAccount = finalAccount / (1 + rate / 100 / 12)**(years*12)

print("Initial deposit value is " + str(initialAccount))
'''





## 2.12
'''
a, b = 0, 1

print("a    b    a ** b")
for number in range(1, 6):
	a = a + 1
	b = b + 1
	print(str(a) + "    " + str(b) + "    " + str(a**b))
'''





## 2.13
'''
integer = eval(input("Enter an integer: "))
digit = 1
while(True):
	if integer // (digit * 10) > 0:
		digit *= 10
	else:
		break

while(True):
	if  digit < 1:
		break

	print(int(integer // digit))
	integer = integer % digit
	digit /= 10
'''





## 2.14 삼각형 공식 찾아볼 것..(또한, 에러 확인)
'''
import math
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

side1 = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
side2 = math.sqrt((y3 - y1)**2 + (x3 - x1)**2)
side3 = math.sqrt((y3 - y2)**2 + (x3 - x2)**2)

s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))	## 중요! 
																## area = math.sqrt(s(s - side1)(s - side2)(s - side3))  
																## 위처럼 곱셈 연산자를 수학처럼 썼을 시 에러 나므로 연산자 신경쓰자.
																## 에러 내용 : 'float' object is not callable
print("The area of the triangle is", round(area, 1))
'''





## 2.15
'''
import math
side = eval(input("Enter the side: "))
area = 3 * math.sqrt(3) / 2 * side**2
print("The area of the hexagon is " + str(round(area, 4)))
'''





## 2.16
'''
v0, v1, t = eval(input("Enter v0, v1, and t: "))
acceleration = (v1 - v0) / t 
print("The average acceleration is", round(acceleration, 4))
'''





## 2.17
'''
pounds = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))
BMI = round(pounds * 0.45359237 / (height * 0.0254)**2, 4)
print("BMI is " + str(BMI))
'''





## 2.18 파이썬 특징 및 람다 함수 볼 것! [시간 조작편]
'''
import time

GMT = eval(input("Enter the time zone offset to GMT: "))

currentTime = time.time()

totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60			## 60 seconds


totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60			## 60 Minutes


totalHours = totalMinutes // 60
currentHours = totalHours % 24				## 24 Hours

currentHours = (currentHours + GMT) % 24	## Current (i.g 12 - 5)

GMTPeriod = "+" + str(GMT) if GMT >= 0 else str(GMT)

print("Current time is " + str(currentHours).zfill(2) + ":" + str(currentMinutes).zfill(2) + ":" + \
		str(currentSeconds).zfill(2) + " GMT:" + GMTPeriod)															## zfill 함수는 숫자 여백에 0을 채워넣어주는 함수이다. 
																													## 뒤의 매개변수는 얼마만큼 넣어줄 수 있는지 명시적으로 기재해줘야 한다.

#print("12".zfill(2))																								## [결과: 12], 그리고 변수 아닌 리터널 상수에 함수에 이용 가능! (파이썬의 특징 1) 
#print("6".zfill(2))																								## [결과: 06]


import time

# Prompt the user to enter the time zone offset to GMT
timeZoneOffset = eval(input("Enter the time zone offset to GMT: "))

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
currentHour = (totalHours + timeZoneOffset) % 24

# Display results
print("Current time is " + str(currentHour) + ":"
    + str(currentMinute) + ":" + str(currentSecond))  
'''




## 2.19 annual 잘 볼 것...
'''
amount = eval(input("Enter investment amount: "))
rate = eval(input("Enter annual interest rate: "))
year = eval(input("Enter number of years: "))
value = round(amount * (1 + rate / 1200)**(year * 12), 2)

print("Accumulated value is " + str(value))
'''





## 2.20
'''
balance, annualInterestRate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))

#interest = balance * (1 + annualInterestRate / 1200)					## 1달간의 이자+원금 수익
interest = balance * (annualInterestRate / 1200)						## 1달간의 이자 수익

print("The interest is", round(interest, 5))
'''





## 2.21
'''
amount = eval(input("Enter the monthly saving amount: "))
account = 0

for i in range (0,6):
		account = (amount + account) * ( 1 + 0.00417 )

print("After the sixth month, the account value is " + str(account))
'''




## 2.22
'''
year = eval(input("Enter the number of years: "))

totalSeconds = year * 365 * 24 * 60 * 60
population = 312032486 + ( totalSeconds // 7 ) - ( totalSeconds // 13 ) + ( totalSeconds // 45 )

print("The population in", number, "years is", population)
'''