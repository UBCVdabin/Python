import random

integer_A = random.randint(1, 100)
integer_B = random.randint(1, 100)

sum = eval(input("Enter the sum of " + str(integer_A) + " and " + str(integer_B) + ": "))
difference = eval(input("Enter the difference of " + str(integer_A) + " – " + str(integer_B)+ ": "))
product = eval(input("Enter the product of " + str(integer_A) + " and " + str(integer_B) + ": "))
quotient = eval(input("Enter the integer part of the quotient from " + str(integer_A) + " / " + str(integer_B) + ": "))

print("\n")

if sum == integer_A + integer_B:
    print("You got the addition right")
else:
    print("Need to work on your addition skills")

if difference == integer_A - integer_B:
    print("You got the difference right")
else:
    print("Need to work on your difference skills")

if product == integer_A * integer_B:
    print("You got the multiplication right")
else:
    print("Need to work on your multiplication skills")

if quotient == integer_A // integer_B:
    print("You got the quotient right")
else:
    print("Need to work on your quotient skills")
