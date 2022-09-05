import random

def BubbleSort(aList):
    for listPass in range(len(aList) - 1):
        for i in range(len(aList) - 1):
            if aList[i] > aList[i+1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]
        print("Pass: " + str(listPass + 1), end = ": ")
        print(aList)

def FindMinPosition(list, startingIndex):
    mini = list[startingIndex]
    miniPos = startingIndex
    for pos in range(startingIndex, len(list)):
        if list[pos] < mini:
            mini = list[pos]
            miniPos = pos
    return miniPos

def SelectionSort(x):
    for pos in range(len(x) - 1):
        minPos = FindMinPosition(x, pos)
        x[pos], x[minPos] = x[minPos], x[pos]
        print("Pass: " + str(pos + 1), end = ": ")
        print(x)

def Selection_Sort(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]



def BinarySearch(list, theItemToFind):
    startidx = 0
    lastidx = len(list) - 1
    mid = (startidx + lastidx) // 2
    
    while startidx <= lastidx:    
        if list[idx] > theItemToFind:
            startidx = mid + 1
        elif list[idx] < theItemToFind:
            lastidx = mid - 1
        else:
            return mid
    
    return - 1


def RemoveAll(someList, someItem):
    while someItem in someList:
        someList.remove(someItem)


def main():

    aList = []
    for i in range(5):
        aList.append(random.randint(50, 60))
    print(aList)

    # 튜플 - 튜플은 리스트와 다르게 각 원소를 변경하거나 삭제할 수도 새로운 원소를 추가할 수도 없는 immutable value 이다.
    bList = (1,2,"dsd")         # 튜플 지정자-> ( )
    alist = (1,2,"asdf", 2) 
    print(alist.__add__(bList)) # 이 자체가 두 튜플이 더한 결과값이 나온다. (그리고 튜플은 또다른 튜플으로만 합성 가능. 만약 튜플과 리스트 또는 int와 같은 변수들과는 합성 불가능함)
    print(alist)                # 이 경우는 두 튜플이 더한 참조 주소가 없는 형태 (즉, alist 형태만 출력함)
                                # concatenate 사슬같이 잇다, 연결하다, 합성하다.

    a, b, c = alist             # 파이썬은 대소문자 구별하기에 대입 연산자 오른쪽에 있는 alist는 aList의 원소들과 확연히 다른 값을 저장하는 변수이다. 
                                # 'a, b, c = alist' 와 같은 statement를 unpacking 이라고 정의한다. tuple과 list 둘다 활용 가능함
                                # unpacking 을 사용하면 일일히 원소를 지정안해도 되기에 편하다. 예) a = alist[0]
                                # 단, 왼쪽에 있는 변수의 갯수는 alist 내재된 원소들의 갯수와 일치시켜야 오류가 발생하지 않는다. 
    print(c)                    # error: too many unpacked values      

    print(FindMinPosition(aList, 1))
    SelectionSort(aList)
    #BubbleSort(aList)

main()

'''
def fun(x): ## x is a deep copy of p
    x.append(100)
    print(x)

p = [0, 50, 25]
fun(p[:])
print(p) ##[0, 50, 25]
'''