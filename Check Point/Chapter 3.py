import math
print(math.sin(2 * math.pi))                # 0 ??? 물어볼것
print(round(math.sin(2 * math.pi)))         # pi는 초월수이기 때문에 컴퓨터 체제에서는 무조건 rounding 해야 정상 값이 나온다.
print(round(math.cos(4 * math.pi)))    # 1
## 3.1 => print(math.sin(2 * math.pi)) 에 대해 물어볼 것!
'''
import math
print(math.sqrt(4))             # 2
print(math.sin(2 * math.pi))    # 0 ??? 물어볼것
print(math.cos(2 * math.pi))    # 1
print(min(2, 2, 1))             # 1
print(math.log(math.e))         # 1
print(math.exp(1))              # 2.718281828459045
print(abs(-2))                  # 2
print(abs(-2.5))                # 2.5
print(math.ceil(-2.5))          # -2
print(math.floor(-2.5))         # -3
print(round(3.5))               # 4
print(round(-2.5))              # -2
print(math.fabs(2))             # 2.0
print(math.fabs(2.5))           # 2.5
print(math.ceil(2.5))           # 3
print(math.floor(2.5))          # 2
print(round(-2.5))              # -2
print(round(2.6))               # 3
print(round(math.fabs(-2.5)))   # 2
'''

## 3.2 Truem The argument for trigonometric functions represents an angle in radians.

## 3.3 degrees to radians 
'''
import math
r = math.radians(47)
print(r)
'''

## 3.4 radians to degrees
'''
import math
r = math.degrees(math.pi / 7)
print(r)
'''

## 3.5
'''
print(ord('1'))     # 따옴표 조심 '', "" 
print(ord('A'))     # ※ '" <- 에러
print(ord('B'))
print(ord('a'))  
print(ord('b'))
print(chr(40))      # chr 함수 경우 Integer를 매개변수로 받음
print(chr(59))
print(chr(79))
print(chr(85))
print(chr(90))
'''

## 3.6              => 앞에 역슬래쉬를 작성하면 됨
#print("\\, \"")     


## 3.7              => 유니코드(=2Byte)는 16진수(4개의 2진수)로 구성되어있다.  1Byte = 8bit (3개의 2진수)
#print("\u4222")    

## 3.8) A를 집어넣으면 결과 값은? D
'''
x = input("Enter a character: ")
ch = chr(ord(x) + 3)
print(ch)               
'''

## 3.9) A와 Z의 문자를 정수로 표현하였을 때의 간격은?  알파벳 개수: 25
'''
x = input("Enter a character: ")
y = input("Enter a character: ")
print(ord(y)-ord(x))
'''

## 3.10
'''
title = "Chapter " + str(1)
print(title)
'''

## 3.11
'''
sum = 2 + 3
print(sum)          # 5
s = '2' + '3'       # '2' + '3' = '2''3' => 문자를 한단위씩 합치는 연산이다.     
print(s)            # 23   
'''

## 3.12
# A) What is an object? Every datum is an object. Object of the same kind have the same type.
# B) What is a method? The method means the function for the object to perform operations. 
# C) What is a variable? The variable is actually a reference to an object.


## 3.13 By using id() and type() functions, I can find id and type.
'''
n = 10
id(n)
type(n)
'''

## 3.14     (B) n is a variable that references an object that holds int value 3.

## 3.15
'''
s = "\tGeorgia\n"
print(s)
print(s.lower())
print(s.upper())
'''

## 3.16
'''
s = "\tGood\tMorning\n"
#print(s)
print(s.strip())            # strip() 함수는 문자 사이에 있는 공백(\t)은 제거를 못하지만 양끝의 여백은 제거 가능하다.
'''

## 3.17     The format function return the string value which is formatted.

## 3.18   	The width is automatically increased to accommodate the size of the actual value.

## 3.19
'''
print(format(57.467657, "9.3f"))                #   57.468
print(format(12345678.923, "9.1f"))             #12345678.9
print(format(57.4, ".2f"))                      #57.40
print(format(57.4, "10.2f"))                    #     57.40
'''

## 3.20
'''
print(format(57.467657, "9.3e"))                #5.747e+01
print(format(12345678.923, "9.1e"))             #  1.2e+07 
print(format(57.4, ".2e"))                      #5.74e+01
print(format(57.4, "10.2e"))                    #  5.74e+01
'''

## 3.21
'''
print(format(5789.467657, "9.3f"))              # 5789.467                  # format() 함수 또한 마지막 숫자가 저절로 반올림 된다.
print(format(5789.467657, "<9.3f"))             #5789.467                   # Banker rounding 형식이다.
print(format(5789.4, ".2f"))                    #5789.40                    
print(format(5789.4, "<.2f"))                   #5789.40
print(format(5789.4, ">9.2f"))                  #  5789.40
'''

## 3.22
'''
print(format(0.457467657, "9.3%"))              #  45.747%                  # 마찬가지로 반올림 신경쓰도록
print(format(0.457467657, "<9.3%"))             #45.747%
'''

## 3.23
'''
print(format(45, "5d"))                         #   45
print(format(45, "<5d"))                        #45
print(format(45, "5x"))                         #   2d                      # 5x 에서 x는 헥사(=16진수)코드 이다. 
print(format(45, "<5x"))                        #2d
'''

## 3.24
'''
print(format("Programming is fun", "25s"))      #Programming is fun         # 디폴트인 경우 숫자와는 다르게 왼쪽 정렬이다.
print(format("Programming is fun", "<25s"))     #Programming is fun
print(format("Programming is fun", ">25s"))     #       Programming is fun
'''