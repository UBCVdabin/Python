#################################
#                               #
##     Problem 1-1 Solution    ##
#                               #
#################################

#-> print(AlexanderNumber(0)) ##outputs 20000
#-> print(AlexanderNumber(1)) ##outputs 40000
#-> print(AlexanderNumber(2)) ##outputs 244.95
#-> print(AlexanderNumber(7)) ##outputs 29.86
def AlexanderNumber(seq):
    sum = 0
    preFirstNumber = 20000      ## The zeroth number of Alexander series is 20000 by definition
    preSecondNumber = 40000     ## The first number of Alexander series is 40000 by definition
    if seq == 0:
        sum = preFirstNumber         

    elif seq == 1:
        sum = preSecondNumber         
       
    else:
        for i in range(2, seq + 1):
            sum = preFirstNumber + preSecondNumber
            if sum > 500:
                sum = round(sum**0.5, 2)
            else:
                sum = round(sum**2, 2)
            preFirstNumber = preSecondNumber
            preSecondNumber = sum
    
    return sum

def main():
    print(AlexanderNumber(0)) ##outputs 20000
    print(AlexanderNumber(1)) ##outputs 40000
    print(AlexanderNumber(2)) ##outputs 244.95
    print(AlexanderNumber(7)) ##outputs 29.86
    print()

main()


#################################
#                               #
##     Problem 1-2 Solution    ##
#                               #
#################################
##outputs
# First 8 terms of Alexander Series:
# 20000, 40000, 244.95, 200.61, 198524.08, 445.79, 446.06, 29.86.

def AlexanderNumber(seq):
    text = ""

    preFirstNumber = 20000      ## The zeroth number of Alexander series is 20000 by definition
    preSecondNumber = 40000     ## The first number of Alexander series is 40000 by definition

    for i in range(0, seq):
        if i == 0:
            text = str(preFirstNumber)
        
        elif i == 1:
            text += ", " + str(preSecondNumber)

        else:
            sum = preFirstNumber + preSecondNumber
            if sum > 500:
                sum = round(sum**0.5, 2)
            else:
                sum = round(sum**2, 2)

            text += ", " + str(sum)            # 20000, 40000, 254
            preFirstNumber = preSecondNumber
            preSecondNumber = sum

    text += "."

    return text


def ShowAlexanderSeries(n):
    if n > 0:
        print("First " + str(n) + " terms of Alexander Series: ")
        return AlexanderNumber(n)
    else: 
        return "We need to input number which is greater than zero."


def main():
    print(ShowAlexanderSeries(0) + "\n")
    
    print(ShowAlexanderSeries(8) + "\n")
    ##outputs
    # First 8 terms of Alexander Series:
    # 20000, 40000, 244.95, 200.61, 198524.08, 445.79, 446.06, 29.86.


    print(ShowAlexanderSeries(4) + "\n")
    ##outputs
    # First 4 terms of Alexander Series:
    # 20000, 40000, 244.95, 200.61.


    print(ShowAlexanderSeries(11) + "\n") 
    ##outputs
    # First 11 terms of Alexander Series:
    # 20000, 40000, 244.95, 200.61, 198524.08, 445.79, 446.06, 29.86, 226503.82, 475.96, 476.42.

main()
