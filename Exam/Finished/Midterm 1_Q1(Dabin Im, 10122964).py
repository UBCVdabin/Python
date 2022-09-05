data = eval(input("Enter a value: "))
x = 0

while data > 0:
    remainder = data % 2
    if remainder == 0:
        x = x + data
    else:
        x = x + data // 10
    data = data // 5

print("Result is " + str(x))