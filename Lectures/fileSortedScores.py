def GetData(fileName):
    ## returns the file content as a list of strings
    fileObject = open(fileName, "r")
    lst = fileObject.readlines()
    fileObject.close()
    return lst

def Clean(listOfStrings):
    for i in range(len(listOfStrings)):
        listOfStrings[i] = listOfStrings[i].strip()

def GetStudentNameScore(aString):
    ## returns a student's name and total score
    res = aString.split(' ')
    name = res[0]
    total = 0
    for i in range(1, len(res)):
        score = float(res[i])
        total += score

    return name, total

def GetStudentsNamesScores(lst):
    mainList = []
    for i in range(len(lst)):
        name, total = GetStudentNameScore(lst[i])
        aList = [name, total]
        mainList.append(aList)

    return mainList

def BubbleSort(aList):
    for listPass in range(len(aList) - 1):
        for i in range(len(aList) - 1):
            if aList[i][1] < aList[i+1][1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]
        # print("Pass: " + str(listPass + 1), end = ": ")
        # print(aList)

def WriteData(lst, fileName):
    ## outputs name and score of student (who got the highest) to fileName
    fileOb = open(fileName, 'w')

    for i in range(len(lst)):
        fileOb.write (lst[i][0] + " " + str(lst[i][1]) + '\n')
    fileOb.close()

def main():
    l = GetData("StudentScores.txt")
    # print(l)
    Clean(l)
    # print(l)
    namesScores = GetStudentsNamesScores(l)
    print(namesScores)
    BubbleSort(namesScores)
    print(namesScores)
    WriteData(namesScores, "Sorted.txt")

main()