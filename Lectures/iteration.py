## 방법 1
#for i in range (20, 5, -3):
#    print(i, end = ", ")

#print(i - 3)


## 방법 2
#for i in range (20, 4, -3):
#    if i > 5:
#        print(i, end = ", ")
#    else:
#        print(i)


## 방법 1
#integer = 20
#while integer > 4:
#    if integer > 5:
#        print(integer, end = ", ")
#    else:
#        print(integer)

#    integer -= 3

## 방법 2
#integer = 20
#while integer > 5:
#    print(integer, end = ", ")
#    integer -= 3

#print(integer)


# 연습 방법 1
integer = eval(input("Enter an integer: "))

for i in range(0, integer - 1):
    print("-", end = "")

print("-")

# 연습 방법 2
integer = eval(input("Enter an integer: "))
count = 1
while count < integer:
    print("-", end = "")
    count += 1

print("-")


#region

#def MakeALine(numStart, numEnd, totalLines):
#    '''
#    This function returns a string.
#    The string contains digit followed by a space,
#    starting from numStart and going all the way to
#    numEnd (inclusive) with a step size of 1.
#    After numEnd + a space, it fills the rezt of the line
#    with spaces, (totalLines - numEnd) * 2 spaces.

#    @params
#    numStart: integer
#    numEnd: integer greater than or equal to numStart
#    totalLines: integer

#    @return
#    a string
#    '''
#    text = ""
#    for i in range(numStart, numEnd + 1, 1):
#        text = text + str(i) + " "
    
#    for i in range(totalLines - numEnd):
#        text = text + "  "

#    return text

###test
#totalLines = int(input("How many lines you want to see?"))

#for line in range(1, totalLines + 1):
#    s = MakeALine(1, line, totalLines)
#    print(s)


#totalLines = int(input("How many lines you want to see?"))
#backup = totalLines
#for line in range(1, totalLines + 1):
#    s = MakeALine(1, backup, totalLines)
#    print(s)
#    backup -= 1

#endregion

def pattern(startIdx = 1, lastIdx = 0, isReverse = False, isSpace = False):
    text = ""
    
    steps = 1
    if isReverse:
        steps = -1
    else:
        lastIdx += 1

    for i in range (startIdx, lastIdx, steps):
        if(isSpace):
            for j in range (i + 1, lastIdx):        # n - 1     // 5, 4, 3, 2, 1, 0
                text += "  "
        for j in range (0, i):                      # n         // 1, 2, 3, 4, 5, 6
            text += str(j+1) + " "
        
        text += "\n"


    return text



integer = eval(input("Enter an integer: "))


# pattern 1
text = pattern(lastIdx = integer)
print(text, end = "")


# pattern 2
text = pattern(startIdx = integer, isReverse = True)
print(text)


# pattern 3
text = pattern(lastIdx = integer - 1)
print(text, end = "")
text = pattern(startIdx = integer, isReverse = True)
print(text)


# pattern 4
text = pattern(lastIdx = integer, isSpace = True)
print(text)

input("Press an enter to finish the console")



