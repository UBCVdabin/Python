# replace(old, new): str
class String():
    def __init__(self, text = ""):
        self.__text = text

    def __str__(self):
        return self.__text

    def getString(self):
        return self.__text

    ## 문자열 왼쪽 공백 제거 
    def lstrip(self, replicator = ""):     ## Check Comprehensive strip  
        length = 0

        if replicator == "":
            replicator = self.getString()

        for i in range(len(replicator)):
            if replicator[i] == ' ':
               length += 1
            else:
               break
        replicator = replicator[length : len(replicator)]
        return replicator



    ## 임의의 문자 찾기 [ 순방향 ]
    def find(self, char):
        idx = -1
        idxAtChar = 0
        originalString = self.getString()


        length = len(char) - 1 ## 배열 크기로 정해야 한다.
        if length > 0:
            for i in range(len(originalString)):
                ## 문자열 체크
                if originalString[i] == char[idxAtChar]:
                    ## 문자열이 1개 일 때..
                    if len(char) == 1:
                        idx = i
                        break
                    ## 문자열이 여러개 일 때..
                    else:
                        ## 문자열이 일치할 경우:
                        if length == idxAtChar:
                            idx = i - length
                            break
                        ## 문자열이 맞는지 계속 체크하기 위해
                        else:
                            idxAtChar += 1
                else:
                    idxAtChar = 0
        return idx



    ## 문자열 오른쪽 공백 제거 
    def rstrip(self, replicator = ""):
        if replicator == "":
            replicator = self.getString

        length = len(replicator)

        for i in range(len(replicator) - 1, -1, -1):
            if replicator[i] == ' ':
               length -= 1
            else:
               break
        replicator = replicator[ : length]
        return replicator




    ## 문자열 양쪽 공백 제거
    def strip(self):
        replicator = self.lstrip()
        replicator = self.rstrip(replicator)
        return replicator




    ## Convert lowercase 
    def lower(self):
        replicator = ""

        for s in self.getString():
            if s >= 'A' and s <= 'Z':
                replicator += chr(ord(s) + 32)
            else:
                replicator += s

        return replicator




    ## Convert uppercase 
    def upper(self):
        replicator = ""

        for s in self.getString():
            replicator += self.makeupper(s)

        return replicator




    ## Capitalize
    def capitalize(self):
        replicator = ""
        originalString = self.getString()
        str = originalString[0]

        replicator += self.makeupper(str[0])
        replicator += originalString[1: len(originalString)]

        return replicator



    def makeupper(self, char):  
        if char >= 'a' and char <= 'z':
                char = chr(ord(char) - 32)

        return char




    ## title 타이틀
    def title(self):
        replicator = ""
        switch = False
        for s in self.getString():

            if not (s >= 'a' and s <= 'z' or s >= 'A' and s <= 'Z' ):
                switch = False

            if not switch and s >= 'a' and s <= 'z':
                replicator += self.makeupper(s)
                switch = True
                continue

            replicator += s

        return replicator




    ## Swapcase
    def swapcase(self):
        replicator = ""

        for s in self.getString():
            if s >= 'A' and s <= 'Z':
                replicator += chr(ord(s) + 32)
            elif s >= 'a' and s <= 'z':
                replicator += chr(ord(s) - 32)
            else:
                replicator += s

        return replicator





    ## 알파벳 [소문자] 체크
    def islower(self):
        if self.isEmpty():
            return False

        for s in self.getString():
            if not (s >= 'a' and s <= 'z'):
                return False

        return True




    ## 알파벳 [대문자] 체크
    def isupper(self):
        if self.isEmpty():
            return False

        for s in self.getString():
            if not (s >= 'A' and s <= 'Z'):
                return False

        return True




    ## 알파벳 [대/소문자] 
    def isalpha(self):
        if self.isEmpty():
            return False

        for s in self.getString():
            if not ((s >= 'a' and s <= 'z') or (s >= 'A' and s <= 'Z')):
                return False

        return True




    ## 공백문자 
    def isspace(self):
        if self.isEmpty():
            return False

        for s in self.getString():
            if s != ' ':
                return False

        return True



    ## 숫자
    def isdigit(self):
        if self.isEmpty():
            return False

        for s in self.getString():
            if not (s >= '0' and s <= '9'):
                return False

        return True
         



    ## 알파벳[대/소문자] + 숫자
    def isalnum(self):
        if self.isEmpty():
            return False

        for s in self.getString():
            if not ((s >= 'a' and s <= 'z') or (s >= 'A' and s <= 'Z') or (s >= '0' and s <= '9')):
                return False

        return True




    ## Null 문자열인지 체크
    def isEmpty(self):
        if len(self.getString()) > 0:
            return False
        else:
            return True




    ## 임의의 문자 찾기 [ 순방향 ]
    def find(self, char):
        idx = -1
        idxAtChar = 0
        orginalString = self.getString()

        length = len(char) - 1 ## 배열 크기로 정해야 한다.
        if length > 0:
            for i in range(len(orginalString)):
                ## 문자열 체크
                if orginalString[i] == char[idxAtChar]:
                    ## 문자열이 1개 일 때..
                    if len(char) == 1:
                        idx = i
                        break
                    ## 문자열이 여러개 일 때..
                    else:
                        ## 문자열이 일치할 경우:
                        if length == idxAtChar:
                            idx = i - length
                            break
                        ## 문자열이 맞는지 계속 체크하기 위해
                        else:
                            idxAtChar += 1
                else:
                    idxAtChar = 0
        return idx





    ## 임의의 문자 찾기 [ 역방향 ]
    def rfind(self, char):
        idx = -1
        idxAtChar = len(char) - 1
        orginalString = self.getString()
        
        if idxAtChar > -1:
            for i in range(len(orginalString) - 1, -1, -1):
                ## 문자열 체크
                if orginalString[i] == char[idxAtChar]:
                    ## 문자열이 1개 일 때..
                    if len(char) == 1:
                        idx = i
                        break
                    ## 문자열이 여러개 일 때..
                    else:
                        ## 문자열이 일치할 경우
                        if idxAtChar == 0:
                            idx = i
                            break
                        ## 문자열이 맞는지 계속 체크하기 위해
                        else:
                            idxAtChar -= 1
                else:
                    idxAtChar = len(char) - 1
        return idx




    ## 중복 문자열 찾기
    def count(self, subStr):
        idx = 0
        length = len(subStr) - 1 ## 배열 크기로 정해야 한다.
        orginalString = self.getString()

        ## subStr 문자열이 없는 경우는 제외
        if length < 0:
            return 0
        
        count = 0

        ## 문자열이 한 개일 때..
        if len(subStr) == 1:
            for s in orginalString:
                if s == subStr[idx]:
                        count += 1

        ## 문자열이 여러 개일 때..
        else:
            for s in orginalString:
                ## 문자열 체크
                if s == subStr[idx]:
                    ## 문자열이 일치할 경우:
                    if length == idx:
                        count += 1
                        idx = 0

                    ## 문자열이 맞는지 계속 체크하기 위해
                    else:
                        idx += 1
                else:
                    idx = 0
                    
                    ## To solve Potential Error 
                    if s == subStr[idx]:
                        idx += 1

        return count


    
    ## 문자 교체하기
    def replace(self, old, new):
        orginalString = self.getString()
        ## 일단 문자가 있는지 먼저 확인
        if not old in orginalString:
            return orginalString

        tempstr = ""
        replicator = ""
        idx = 0
        length = len(old) - 1 ## 배열 크기로 정해야 한다.

        if length > -1:
            for s in orginalString:
                ## 문자열 체크
                if s == old[idx]:
                    ## 문자열이 1개 일 때..
                    if len(old) == 1:
                        replicator += new

                    ## 문자열이 여러개 일 때..
                    else:
                        ## 문자열이 일치할 경우:
                        if length == idx:
                            tempstr = ""
                            replicator += new
                            idx = 0
                           
                        ## 문자열이 맞는지 계속 체크하기 위해
                        else:
                            tempstr += s
                            idx += 1
                else:
                    idx = 0
                    replicator += tempstr + s
                    tempstr = ""

        return replicator


    ## 시작 문자열 비교
    def startswith(self, str, start = 0, end = -1):
        orginalString = self.getString()

        ## idx 음수 또는 기존 문자열 보다 클 경우
        if start < 0 or start > len(orginalString) - 1:
            return False
        
        ## 마지막 인덱스가 기존 문자열보다 클 경우
        if end != -1 and (start > end or end > len(orginalString)):
            return False

        ## 기존 end 초기값이 변경되지 않았을 때
        if end == -1:
            end = len(self.text) - 1

        ## idx가 양수이면서 배열에 넘어갔을 경우 False 반환
        if len(orginalString) < start + len(str):
            return False
        
        ## checking
        for s in str:
            if orginalString[start] == s and start < end:
                start += 1
                continue
            else:
                return False
      
        return True




    ## 마지막 문자열 비교
    def endswith(self, str, start = 0, end = -1):
        orginalString = self.getString()

        ## idx 음수 또는 기존 문자열 보다 클 경우
        if start < 0 or start > len(orginalString) - 1:
            return False

        ## 마지막 문자열 위치로 고정 end = -1 [default value]
        if end == -1:
            end = len(orginalString)

        ## 마지막 인덱스가 기존 문자열보다 클 경우
        if start > end or end > len(orginalString):
            return False

        ## 배열의 시작 인덱스 : 0 [결론: end = end - 1]
        start -= 1
        end -= 1

        ## idx가 양수이면서 배열에 넘어갔을 경우 False 반환
        if end - len(str) < 0:
            return False

        ## checking
        for s in reversed(str):
            if self.__text[end] == s and start < end:
                end -= 1
                continue
            else:
                return False
      
        return True




    ## 가운데 정렬
    def center(self, width):
        orginalString = self.getString()
        if len(orginalString) > width:
            return orginalString
    
        replicator = ""
    
        left = (width - len(orginalString)) // 2
        right = left + (width - len(orginalString)) % 2
    
        for i in range(left):
            replicator += ' '
    
        replicator += orginalString
    
        for i in range(right):
            replicator += ' '
    
        return replicator
    
    

    
    ## 왼쪽 정렬
    def ljust(self, width):
        orginalString = self.getString()
        if len(orginalString) > width:
            return orginalString

        replicator = ""

        width -= len(orginalString)
        replicator += orginalString

        for i in range(width):
            replicator += ' '
    
        return replicator
    
    
    
    
    ## 오른쪽 정렬
    def rjust(self, width):
        orginalString = self.getString()
        if len(orginalString) > width:
            return orginalString
        
        replicator = ""
    
        width -= len(orginalString)
    
        for i in range(width):
            replicator += ' '
    
        replicator += orginalString
    
        return replicator
    

def main():
    a = "asasaasaasasasssasaa"
    print(a.count("saa"))

    asd = String(a)
    print(asd.count("saa"))



main()


#region
'''
def MyFind(text, old):
    for i in range(len(text)):
        if text[i] == old[0]:
            subString = text[i : i+len(old)]
            if subString == old:
                return i
    return -1

# print(MyFind("python p ypthon p", "py"))

def ReplaceFirst(text, old, new):
    if old not in text:
        return text
    
    newText = ""
    
    position = MyFind(text, old)

    newText = text[:position]
    newText += new
    newText += text[position + len(old):]

    return newText

def ReplaceAll(text, old, new):
    while ReplaceFirst(text, o, n) != text:
        text = ReplaceFirst(text, o, n)
    return text

text = "pypython python p"
o = "py"
n = "java"
print(ReplaceAll(text, o, n))
'''
#endregion