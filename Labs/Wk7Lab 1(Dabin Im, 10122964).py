integer = eval(input("Enter an integer: "))

text = ""
for i in range (1, integer + 1):
    if integer % i == 0:
        text = text + str(i)
        print(str(i), end = "\n" if integer == i else ", ")
        