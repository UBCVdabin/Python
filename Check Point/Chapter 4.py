s## 4.1 List six comparison operators
#      A] >=, ==, <=, !=, >, <

## 4.2
'''
i = int(True)       # 1
j = int(False)      # 0

b1 = bool(4)        #True
b2 = bool(0)        #False

print(i)
print(j)
print(b1)
print(b2)
'''

## 4.3
'''
import random
random.randint(0, 19) or random.randrange(0, 20)
'''

## 4.4
'''
import random
random.randint(10, 19) or random.randrange(10, 20)
'''

## 4.5
'''
import random
random.randint(10, 50) or random.randrange(10, 51)
'''

## 4.6
'''
import random
random.randint(0, 1) or random.randrange(0, 2)
'''

## 4.7
'''
if y > 0:
	x = 1
'''

## 4.8
'''
if score > 90:
	pay *= 1.03		# The statement that increases pay by 3% 임금율이 상승함으로 기존 월급에서 3퍼센트를 더한뒤에 
					# 곱하면 임금률이 상승한 금액이 결과값으로 나온다.
'''

## 4.9
'''
if score > 90:
	pay *= 1.03
else:
	pay *= 1.01
'''

## 4.10
# number 가 30 일 경우
# A)	30 is even.
#		30 is odd.		
# B)	30 is even.

# number 가 35 일 경우
# A)	35 is odd.
# B)	35 is odd. 		 


## 4.11
# 기존) x is 3
# A) z is 7
# B) 없다.

## 4.12
# 기존) x is 2
# A) 없다
# B) z is 6

## 4.13
'''
if score >= 60.0 and score < 70.0:
	grade = 'D'
elif score >= 70.0 and score < 80.0:
	grade = 'C'
elif score >= 80.0 and score < 90.0:
	grade = 'B'
elif score >= 90.0 and score <= 100.0:
	grade = 'A'
else:
	grade = 'F'
'''

## 4.14 (A), (C)

## 4.15 -> 문제 이해도부터 파악해야 할 것..
# newline = count % 10 == 0

## 4.16 ->	(B) is better. Both conditions in (A) are tested. 
#			In (B) the condition is tested only once.

## 4.17
# - 14 인 경우 
# a) 14 is even
# b) 14 is even

# - 15 인 경우
# a) 15 is multiple of 5
# b) 15 is multiple of 5

# - 30 인 경우
# a) 30 is even
#	 30 is multiple of 5
# b) 30 is even

## 4.18 Both are correct. but (B) is better

## 4.19
'''
if income <=10000:
	tax = income * 0.1
elif income > 10000 and income <= 20000:
	tax = 1000 + (income - 10000) * 0.15
else:
	tax = 8350 * 0.10 + (33950 -8350) * 0.15 + (82250 - 33950) * 0.25 + (171550-82250) * 0.28 + \
	(income - 171550) * 0.33

print(tax)
'''

## 4.20   if x = 1
# True and (3 > 4)				-> false
# not (x > 0) and ( x > 0)		-> false
# (x > 0) or (x < 0)			-> true
# (x != 0) or (x == 0)			-> true
# (x >= 0) or (x < 0)			-> true
# (x != 1) == not ( x == 1)		-> true

## 4.21
# 답 : num >= 1 and num <= 100

## 4.22
# 답 : (num >= 1 and num <= 100) or num < 0

## 4.23   if x = 4, y = 5
# x >= y >= 0					-> true
# x <= y >= 0					-> false
# x != y == 5					-> true
# (x != 0) or (x == 0)			-> true

## 4.24 (a)

## 4.25
# if ch == 'A', -> true
# if ch == 'p', -> false
# if ch == 'E', -> true
# if ch == '5', -> false

## 4.26		input : 2,3,6
'''
x, y, z = eval(input("Enter three numbers: "))

print("(x < y and y < z) is", x < y and y < z)		# True
print("(x < y or y < z) is", x < y and y < z)		# True
print("not (x < y) is", not (x < y))				# False
print("(x < y < z) is", x < y < z)					# True
print("not(x < y < z) is", not (x < y < z))			# False
'''

## 4.27
# age > 13 and age < 18

## 4.28
# weight > 50 or height > 160

## 4.29
# weight > 50 and height > 160

## 4.30																	※ De Morgan's law 다시 볼것...
# weight > 50 or height > 160 and not(weight > 50 and height > 160)

## 4.31																	※ print 안에 if 절 볼 것!
'''
x, y, z = eval(input("Enter three numbers: "))
print("sorted" if x < y and y < z else "not sorted")					# sorted
'''

## 4.32
count = 11
#ticketPrice = 20 if age >= 16 else 10 
print(count, end = "\n" if count % 10 == 0 else " ")			# 앞에 count 변수는 값을 출력하는 것이며, 뒤에 count 조건문으로 
																# 뒤의 개행문자를 선택할 수 있다.

## 4.33
#(a)
'''
if > 10:
	score = 3 * scale
else:
	score = 4 * scale
'''
#(b)
'''
if income > 10000:
	tax = income * 0.2
else:
	tax = income * 0.17 + 10000
'''
#(c)
'''
if number % 3 == 0:
	print(i)
else:
	print(j)
'''

## 4.34		※ The precedence order of the Boolean operators are not, and, or in this order.
#1.True		※ 순서 기억할 것! ( 우선순위 : not > and > or 연산자 순 ) 즉, or 연산자가 제일 마지막으로 연산한다.
#2.True

## 4.35		답 : True

## 4.36		계산 순서
'''
※ 2 * 2 - 3 > 2 and 4 - 2 > 5
1) 4 - 3 > 2 and 4 - 2 > 5
2) 1 > 2 and 2 > 5
3) (False) and (False)

결과: False

※ 2 * 2 - 3 > 2 or 4 - 2 > 5
1) 4 - 3 > 2 or 4 - 2 > 5
2) 1 > 2 or 2 > 5
3) (False) or (False)

결과: False
'''

## 4.37		답 : 모두 다 같다.