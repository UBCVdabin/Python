def MakingTerms(n):
    return 1/n


def main():
    integer = eval(input("Enter an integer: "))

    if integer % 2 == 0:
        integer = integer - 1

    total = 0
    switch = False
    for i in range(1, integer + 1, 2):
        if switch:
            total -= MakingTerms(i)
            switch = False
        else:
            total += MakingTerms(i)
            switch = True

    print(format(total, "<12.11f"))
    
main()