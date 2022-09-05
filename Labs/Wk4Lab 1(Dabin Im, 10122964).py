import sys

number = input("Enter the number: ")

if(number.isdigit() is False):
    print("Wrong number...")
    sys.exit(0)

total = 0
k = 0
number = int(number)

while (k < number):
    val = input("Enter the value: ")

    if (val.isdigit() is False):
        print("Wrong number...")
        sys.exit(0)

    val = int(val)

    if int(val) > 0:
        total = total + val
    k = k + 1

print("Total =", total)
