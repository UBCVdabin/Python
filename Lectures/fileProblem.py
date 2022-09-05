
def GetData(fileName):

    fileObject = open(fileName, "r")

    lst = fileObject.readlines()
    fileObject.close()

    return lst


def WriteData(name, score, fileName):
    '''
    File processing:
    Step First: open the file in the correct mode
        Do file processing (output the data to the file)
    Step Last: close the file
    '''
    fileObject = open(fileName + ".txt", 'w') 
    ##to send data to a file mode is either "w" (open the file remove all contents before writing) or 
    ## "a" (open the file and add data to exisiting content in the file i.e. do not remove existing content)
    ## in BOTH modes is file does not exist then it will be created for you
    fileObject.write("Name: " + str(name) + "\n")
    fileObject.write("Total Score: " + str(score) + "\n")

    fileObject.close()


def GetStudentNameScore(aString):
    alist = aString.split()
    name = alist[0]
    totalScore = 0

    for i in range (1, len(alist)):
        totalScore += int(alist[i])

    return name, totalScore


def Process(listOfStrings):
    name = ""
    totalScore = 0
    for i in range (len(listOfStrings)):
        tempname, tempScore = GetStudentNameScore(listOfStrings[i].strip())

        if tempScore > totalScore:
            name = tempname
            totalScore = tempScore

    WriteData(name, totalScore, "results")


# X = []
# ReadStrings(X)
StudentScores = []
StudentScores = GetData("StudentScores.txt")
Process(StudentScores)



