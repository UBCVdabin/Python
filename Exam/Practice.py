def CleanString(aString):
    return aString.strip()


def CountWords(aString):
    return len(aString.split())


def ProcessList(listOfStrings):
    for i in range(len(listOfStrings)):
        print("String " + str(i+1) + " has " + str(Process(listOfStrings[i])) + " words.")


def Process(aString):
    aString = CleanString(aString)
    return CountWords(aString)

def ReadString(aList):
    ## if user inputs an empty string then stop taking inputs
    userInput = input("Enter a string: ")
    while userInput != "":
        aList.append(userInput)
        userInput = input("Enter a string: ")

def WriteFile():
    f = open("file.txt", 'w')
    f.write("   This is the first string.   \n")
    f.write("    This is the second string.      \n")
    f.write("    This strings may be dirty.    \n")
    f.write("      We have to count the number of words in each string after cleaning them.    \n")
    f.close()

def ReadFromFile(X):
    f = open("file.txt", 'r')
    while True:
        line = f.readline()
        if not line: break
        X.append(line)
    f.close()

def main():
    count = 0
    WriteFile()
    #X = [ "   This is the first string.   ", "    This is the second string.      ", \
    #    "    This strings may be dirty.    ", \
    #    "      We have to count the number of words in each string after cleaning them.    \n"]
    X = []
    ReadFromFile(X)
    #ReadString(X)

    ProcessList(X)

main()

#region 선생님 코드

'''
Suppose that there is a list of strings. For example,

X = [“    This is the first string.      ”, “      This is the second string.   ”, “These strings may be dirty.		”, “     We have to count the number of words in each string after cleaning them.     \n”]

Dirty = strings may have white spaces (single spaces, tab spaces, new line) before and after

Write a Python program to count the number of words in each list item after cleaning it (remove spaces before and after from each string before processing it).
Hint: 
•	Strip method of strings
•	X[0] is the first string, X[i] would be the i-th string in X
•	Number of words in a string is one more than the number of spaces in the clean string. Assume words are separated by a single space.

Functions are mandatory. For example, Process(aString), CleanString(aString), 
CountWords(aString)

'''

def ReadStrings(aList):
    ## if user inputs an empty string then stop taking inputs
    userInput = "dummy string"
    while userInput != "":
        userInput = input("Enter a string")
        if userInput != "":
            aList.append(userInput)
    # return aList ## not necessary cause aList changing means X changing (memory address of X is sent to this function)

def ReadFromFile(fileName):
    '''
    Dealing with files:
    open the file
        do some file task (get data from file)
    close the file
    '''
    fileObject = open(fileName, "r") ## to get data from a file mode is "r"
    ## if file does not exist then there will be an ERROR
    ## read data from a file
    ## readLines returns a list of strings where each line in the file is a string in the list
    lst = fileObject.readlines()
    fileObject.close()

    return lst ## return is necessary cause lst is in a different memory address than aList

def Clean(aString):
    cleanString = aString.strip()
    return cleanString

def CountWords(aString):
    if len(aString) == 0:
        return 0
    count = 1
    for i in range(len(aString)):
        if aString[i] == ' ':
            count += 1
    return count

def WriteData(data, fileName):
    '''
    File processing:
    Step First: open the file in the correct mode
        Do file processing (output the data to the file)
    Step Last: close the file
    '''
    fileObject = open(fileName, "a") 
    ##to send data to a file mode is either "w" (open the file remove all contents before writing) or 
    ## "a" (open the file and add data to exisiting content in the file i.e. do not remove existing content)
    ## in BOTH modes is file does not exist then it will be created for you

    fileObject.write(str(data) + "\n")

    fileObject.close()


def ProcessList(listOfStrings):
    for i in range(len(listOfStrings)):
        cString = Clean(listOfStrings[i])
        # print(cString)
        numWords = CountWords(cString)
        WriteData(numWords, "Output.txt")
        # print("String " + str(i+1) + " has " + str(numWords) + " words.")

# X = []
# ReadStrings(X)
X = []
X = ReadFromFile("input.txt")
ProcessList(X)

#endregion