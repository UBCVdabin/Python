## 5.1 
# count < 100 is always True at Point A.  
# count < 100 is always False at Point C.  
# count < 100 is sometimes True or sometimes False at Point B.
'''
count = 0
while count < 100:
    # Point A
    print("Programming is fun!")
    count += 1
    # Point B

# Point C
'''

## 5.2 
# The value of the number variable would be zero. That meaning is it is possible to ignore the while repeation statement.

## 5.3 
# (a) infinite
# (b) infinite
# (c) The loop body is executed nine times. The printout is 2, 4, 6, 8 on separate 

## 5.4
# (a) infinite
# (b) infinite
# (c) has an indentation error.

## 5.5
# max is 5
# number 0

## 5.6
# sum is 14
# count is 4
'''
number = 0
sum = 0 

for count in range(5):
    number = eval(input("Enter an integer: "))
    sum += number

print("sum is", sum)        # sum is 14
print("count is", count)    # count is 4
'''

## 5.7
# advantages of using for loops
# - all user do not need to declare countable variable.
# - by using range function, you are able to read the code.
# - It is also easy to understand code.
'''
number = 0
sum = 0
count = 0
while count <= 4:
    number = eval(input("Enter an integer: "))
    sum += number
    count += 1

print("sum is", sum)
print("count is", count)
'''

## 5.8
'''
sum = 0
for i in range(1001):
    sum = sum + i
print(sum)

## convert from for loops to while loops
sum = 0
i = 0
while i <= 1000:
    sum = sum + i
    i += 1

print("sum is", sum)
'''

## 5.9
# Can you always convert a while loop into a for loop? Not in Python. 
# For example, you cannot convert the while loop in Listing 5.3, GuessNumber.py, to a for loop.
'''
i = 1
sum = 0 

while sum < 10000:
    sum = sum + i
    i += 1

print("sum is", sum)

sum = 0

for i in range(0, 10000):
    if(sum < 10000):
        sum = sum + i
    else:
        break

print("sum is", sum)
'''

## 5.10
# (A) n times
# (B) n times
# (C) n - 5 times
# (D) (n - 5)/3 times

## 5.11 다시 볼 것...
#region

# (A) 0 0 1 0 1 2 0 1 2 3 
'''A 실행 순서 및 코드
for i in range (1, 5):
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1

# 1      0          0
# 1      1          
# 2      0          0          
# 2      1          1          
# 2      2                   
# 3      0          0          
# 3      1          1          
# 3      2          2         
# 3      3                   
# 4      0          0          
# 4      1          1          
# 4      2          2         
# 4      3          3        
# 4      4                  
'''



# (B) 
# ****
# ****
# 2 ****
# 3 2 ****
# 4 3 2 **** 
'''B 코드
i = 0
while i < 5:
    for j in range(i, 1, -1):
        print(j, end = " ")
    print("****")
    i += 1
'''



# (C)
# 1xxx2xxx4xxx8xxx16xxx
# 1xxx2xxx4xxx8xxx
# 1xxx2xxx4xxx
# 1xxx2xxx
# 1xxx



# (D)
# 1G
# 1G3G
# 1G3G5G
# 1G3G5G7G
# 1G3G5G7G9G
#endregion

## 5.12
# No. 
# "Try n1 = 3 and n2 =3" 이건 정답이 될 수 없다. 애시당초 진입을 안하는데 왜 써있는지 모르겠다.
# while 문의 조건처럼 if 절에도 동일하게 써야한다.
'''
k = 2
n1 = 36
n2 = 24
while k <= n1 / 2 and k <= n2 / 2:
    if (n1 / 2) % k == 0 and (n2 / 2) % k == 0:
        gcd = k
    k += 1
print(gcd)
'''

## 5.13
# The keyword break is used to exit the current loop. The program in (A) will terminate. The output is Balance is 1.
# The keyword continue causes the rest of the loop body to be skipped for the current iteration. The while loop will not terminate in (B).

## 5.14 continue 문은 while 문 끝자락에 가게 해준다. 다시 말하자면, 어떤 하나의 인덱스 안에 반복과정 중에 continue를 만나면 모든 동작을 멈춘 뒤에 다음 인덱스를 실행할 준비를 한다라는 뜻.
# If a continue statement is executed inside a for loop, the rest of the iteration is skipped, then the action-after-each-iteration is performed and the loop-continuation-condition is checked. 
# If a continue statement is executed inside a while loop, the rest of the iteration is skipped, then the loop-continuation-condition is checked. 
'''
i = 0

while i < 4:
    if i % 3 == 0: 
     	  i += 1
    	  continue
    sum += i
    i += 1
'''

## 5.15 continue 문 대신 조건문으로 조작하면 됨
'''
sum = 0
number = 0

while number < 20 and sum < 100:
    number += 1
    sum += number

print("The number is " + str(number))
print("The sum is " + str(sum))


sum = 0
number = 0

while (number < 20): 
    number += 1
if (number != 10 and number != 11): 
        sum += number

print("The sum is " + str(sum))
'''


## 5.16
# (A)
# 1
# 2
# 1
# 2
# 2
# 3

# (B)
# 1
# 2
# 1
# 2
# 2
# 3
