def IsPrime(n):
    '''
    This function returns True if n is a prime integer,
    otherwise return False.
    We assume n is an integer.

    @params
    n: integer

    @return
    Boolean
    '''
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    
    if count == 2:
        return True
    else:
        return False

def main():
    count = 1                   # Count = N - 1
    totalCount = 0              # TotalCount = N
                                # So, we can print ", " n - 1 times and the last print can excute line change.

    for i in range(2, 21, 1):
        if IsPrime(i):    
            totalCount += 1


    for i in range(2, 21, 1):
        if IsPrime(i):  
            if count < totalCount:
                print(i, end = ", ")
                count += 1

            else:
                print(i)

main()