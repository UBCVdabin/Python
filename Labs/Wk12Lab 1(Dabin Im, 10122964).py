class String():
    def __init__(self, text = ""):
        self.__text = text

    def __str__(self):
        return self.showText()

    def showEachCharacter(self, exceptChar = ""):
        text = self.__text
        for i in range(len(text) - 1, -1, -1):
            if exceptChar != "" and text[i] == exceptChar:
                break
            
            print(text[i])

    def showText(self):
        return self.__text

    def RemoveSpace(self, All = False):
        str = self.__text
        replicator = ""
        
        
        ## lstrip
        length = 0 
        for s in self.__text:
            if s == ' ':
                length += 1
            else:
                break

        replicator = str[length : len(str)]

        ## rstrip
        length = len(replicator)
        for s in reversed(replicator):
            if s == ' ':
                length -= 1
            else:
                break

        replicator = replicator[ : length]
        
        if All:
            temp = replicator
            replicator = ""
            for s in temp:
                if s == ' ':
                    continue
                else:
                    replicator += s

        return replicator




def main():
    s = String("  abcd  ")
    print(s)
    print(len(s.showText()))
    print(s.RemoveSpace())
    print(len(s.RemoveSpace()))
    

    s = String("     ")
    print(s)
    print(len(s.showText()))
    print(s.RemoveSpace())
    print(len(s.RemoveSpace()))

    s = String("  ab cd  ")
    print(s)
    print(len(s.showText()))
    print(s.RemoveSpace())
    print(len(s.RemoveSpace()))
    print(s.RemoveSpace(True))

main()


## 교수님 버전
def RemoveSpaces(someString):
    ## find first non-space character
    for i in range(len(someString)):
        if someString[i] != ' ':
            break
    start = i

    ##find the last non-space character
    for i in range(len(someString) - 1, -1, -1):
        if someString[i] != ' ':
            break
    end = i

    return someString[start : end + 1]

def main():
    s = "         "
    t = RemoveSpaces(s)
    print(t)
    print(len(t))

    rev = s[::-1] ##reverses a string


main()
