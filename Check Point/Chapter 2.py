## 2.1
'''
width = 5.5
height = 2
print ("area is", width * height)
'''

## 2.2
'''
miles = 100
kilometers = miles * 1.609
print("kilometers:", kilometers) ## kilometer : 160.9
'''

## 2.3 
#-> answer: by using the eval() function, it can convert the input data of string to a numeric value.\

## 2.4
'radius = eval(input("Enter a radius: "))' #->  Throw the error which is unexpected EOF while parsing

## 2.5 -> the line continuation symbol (\)

## 2.6 -> miles, Test, radius

## 2.7 -> variables are the names that reference values stored in memory

## 2.8 -> variables must be left side.

## 2.9
'''
x = y = z = 0       ##  x, y, z get the same value.
print(x+y+1.0,y,z)
'''

## 2.10
'''
a = 1 
b = 2 
print(a,b)
a, b = b, a         ## they can swap the value each other.
print(a,b)
'''

## 2.11
'''
print(42 / 5)                           ## 8.4
print(42 // 5)                          ## 8
print(42 % 5)                           ## 2
print(40 % 5)                           ## 0
print(1 % 2)                            ## 1
print(2 / 1)                            ## 2.0
print(45 + 4 * 4 - 2)                   ## 59
print(45 + 43 % 5 * (23 * 3 % 2 ))      ## 48
print(5 ** 2)                           ## 25
print(5.1 ** 2)                         ## 26.01
'''

## 2.12
'print(100 % 7)                          ## Friday' 

## 2.13
'''
print(25 / 4)                           ## 6.25
print(25 // 4)                          ## 6
'''

## 2.14
'print(4 / 3(r + 24) - 9( a + b * c) + (3 + d(2+a))/(a+b*d))'

## 2.15
'''
m = 1
r = 2
print(m*r**2)
'''

## 2.16
'''
a = 1
a += 4              ## 5
print(a)

a = 1
a -= 4              ## -3
print(a)

a = 1
a *= 4              ## 4
print(a)

a = 1
a /= 4              ## 0.25
print(a)

a = 1
a // 4              ## 몫이 0.25이지만 정수부분만 보여주는 관계로 반올림을 한다. 따라서, 결과는 1 이다   
print(a)

a = 1
a %= 4              ## 1
print(a)

a = 1
a = 56 * a + 6      ## 62
print(a)
'''

## 2.17
'''
value = 4.6 
print(int(value))       ## remove the float part without a round
'''

## 2.18  -> 다시 볼 것..
'''
value = 4.6
print(int(value))               ## 4
print(round(value))             ## 5
print(eval("4 * 5 + 2"))        ## 22.00
print(int("04"))                ## 4
#print(int("4.5"))              ## Error ! => invalid literal for int() with base 10: '4.5' [=float number..]
#print(eval("04"))              ## Error ! => leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers 
'''

## 2.19 -> The epoch is the point when time starts. 
#          1980 was the year when the UNIX operating system was formally introduced

## 2.20 -> time.time() plays the role to return the current time in seconds
#          as a float value with millisecond precision.

## 2.21  -> To obtain the seconds, use the this formula "time.time() % 60"