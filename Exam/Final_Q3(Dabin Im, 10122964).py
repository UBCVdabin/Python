def LDS(lst):
    count = 0
    tempcount = 0
    if len(lst) < 2:
        return 0

    for i in range (len(lst) - 1):
        if lst[i] > lst[i+1]:
            count += 1

        else:
            tempcount = count if count > tempcount else tempcount
            count = 0

    count = count if count > tempcount else tempcount

    return count

def main():
    print(LDS([5, 5, 4, 2, 2]))         # returns 2
    print(LDS([1, 2, 5, 5, 2]))         # returns 1
    print(LDS([]))                      # returns 0
    print(LDS([3]))                     # returns 0
    print(LDS([50,40,65,4,3,9,4,2]))    # returns 2
    print(LDS([50,40,30,4,3,2,1]))      # returns 6

main()