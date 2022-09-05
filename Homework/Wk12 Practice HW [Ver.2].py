class myString():
    def __init__(self, text):
        self.__text = text

    def __str__(self):
        return self.getString()



    ## Function Method [Private]
#region 
    def __lstripProcess(self, text):
        length = 0

        for s in text:
            if s == ' ':
               length += 1
            else:
               break

        text = text[length : len(text)]
        return text



    def __rstripProcess(self, text):
        length = len(text)

        for s in reversed(text):
            if s == ' ':
               length -= 1
            else:
               break

        text = text[ : length]
        return text



    ## islower => True 
    def __checklower(self, char):
         if not (char >= 'a' and char <= 'z'):
             return False
         return True



    def __checkupper(self, char):
         if not (char >= 'A' and char <= 'Z'):
             return False
         return True




    def __checkdigit(self, char):
         if not (char >= '0' and char <= '9'):
             return False
         return True




    def __checkspace(self, char):
        if char != ' ':
            return False

        return True




    def __makeupper(self, char):  
        return chr(ord(char) - 32)




    def __makelower(self, char):  
        return chr(ord(char) + 32)




    def __makespace(self, count):
        space = ""
        for i in range(count):
            space += ' '
        return space




    ## is Null ? Checking Method
    def __isEmpty(self):
        if len(self.getString()) > 0:
            return False
        else:
            return True



    def __findProcess(self, idx, str):
        originalString = self.getString()
        
        if originalString[idx] == str[0]:
            subString = originalString[idx : idx + len(str)]
            
            if subString == str:
                return idx

        return -1

#endregion



    def getString(self):
        return self.__text



    def lstrip(self):     
        return self.__lstripProcess(self.getString())



    def rstrip(self):
        return self.__rstripProcess(self.getString())



    def strip(self):
        text = self.__lstripProcess(self.getString())
        text = self.__rstripProcess(text)
        return text



    ## Convert lowercase 
    def lower(self):
        text = ""

        for s in self.getString():
            if self.__checkupper(s):
                text += self.__makelower(s)
            else:
                text += s

        return text



    ## Convert uppercase 
    def upper(self):
        text = ""

        for s in self.getString():
            if self.__checklower(s):
                text += self.__makeupper(s)
            else:
                text += s

        return text



    ## Capitalize
    def capitalize(self):
        text = ""
        originalString = self.getString()
        
        text = originalString[0]
        if self.__checklower(text):
            text = self.__makeupper(text)

        text += originalString[1: len(originalString)]

        return text



    ## title 
    def title(self):
        text = ""
        
        switched = False
        for s in self.getString():
            if self.__checkspace(s):
                switched = False

            if not switched and self.__checklower(s):
                text += self.__makeupper(s)
                switched = True
                continue

            text += s

        return text




    ## Swapcase
    def swapcase(self):
        text = ""

        for s in self.getString():
            if self.__checkupper(s):
                text += self.__makelower(s)
            elif self.__checklower(s):
                text += self.__makeupper(s)
            else:
                text += s

        return text





    ## Alpabet Lower Check
    def islower(self):
        if self.__isEmpty():
            return False

        for s in self.getString():
            if not self.__checklower(s):
                return False

        return True




    ## Alpabet Upper Check
    def isupper(self):
        if self.__isEmpty():
            return False

        for s in self.getString():
            if not self.__checkupper(s):
                return False

        return True




    ## Integrated Alpabet 
    def isalpha(self):
        if self.__isEmpty():
            return False

        for s in self.getString():
            if not (self.__checkupper(s) or self.__checklower(s)):
                return False

        return True




    ## Space 
    def isspace(self):
        if self.__isEmpty():
            return False

        for s in self.getString():
            if not self.__checkspace(s):
                return False

        return True



    ## Number
    def isdigit(self):
        if self.__isEmpty():
            return False

        for s in self.getString():
            if not self.__checkdigit(s):
                return False

        return True
         



    ## Integrated Alpabet + Number
    def isalnum(self):
        if self.__isEmpty():
            return False

        for s in self.getString():
            if not (self.__checklower(s) or self.__checkupper(s) or self.__checkdigit(s)):
                return False

        return True




   ## Center Align
    def center(self, width):
        originalString = self.getString()
        
        if len(originalString) > width:
            return originalString

        text = ""

        left = (width - len(originalString)) // 2
        right = left + (width - len(originalString)) % 2

        text += self.__makespace(left)
        text += originalString
        text += self.__makespace(right)

        return text




    ## Left Align
    def ljust(self, width):
        originalString = self.getString()
        
        if len(originalString) > width:
            return originalString

        text = ""

        width -= len(originalString)
        text += originalString
        text += self.__makespace(width)
    
        return text
    
    
    
    
    ## Right Align
    def rjust(self, width):
        originalString = self.getString()

        if len(originalString) > width:
            return originalString
        
        text = ""
    
        width -= len(originalString)
        text += self.__makespace(width)
        text += originalString
    
        return text




    ## Index Validation 
    def __isqualified(self, str, start, end):
        originalString = self.getString()
        length = len(originalString)
        
        if str == "":
            return False

        if start < 0 or start > length - 1:
            return False

        if start > end or end > length:
            return False

        if length < start + len(str):
            return False

        return True




    ## Find
    def find(self, str, start = 0, end = -1):
        originalString = self.getString()

        if end == -1:
            end = len(originalString)

        if not self.__isqualified(str, start, end):
            return -1

        for i in range(start, end):             ## keep finding value successively.
            idx = self.__findProcess(i, str)
            if idx != -1:                       
                return idx
        return -1



    ## rFind
    def rfind(self, str, start = 0, end = -1):
        originalString = self.getString()

        if end == -1:
            end = len(originalString)

        if not self.__isqualified(str, start, end):
            return -1

        end = end - (len(str) - 1)          # Start Point 
                                            # if char is 1 => len(originalString) - 1 
                                            # if char is more than 1 => len(originalString) - 1 - (len(char) - 1)
                                            # So, I need to subtract 1

        # Settings => Because of Repeation Property
        start -= 1
        end -= 1

        for i in range(end, start, -1):
            idx = self.__findProcess(i, str)
            if idx != -1:                       
                return idx
        return -1



    ## Replace
    def replace(self, old, new):
        originalString = self.getString()

        if not old in originalString:
            return originalString

        text = ""
        idx = 0
        
        while True:
            position = self.find(old, idx)

            if position == -1:
                text += originalString[idx:]
                break

            text += originalString[idx:position]
            text += new
            idx = position + len(old)               # position gives us Start Point = 0. 
                                                    # So, we don't need to care about start point. 

        return text



    ## count
    def count(self, subStr, overlap = False):
        idx = 0
        count = 0
        length = len(subStr)
        originalString = self.getString()

        if not subStr in originalString:
            return count

        ## if len(subStr) is zero  
        if length == 0:
            return count
        
        idx = self.find(subStr, start = idx)
        
        while idx != -1:
            count += 1
            if overlap:
                idx = self.find(subStr, start = (idx + 1)) # allow or not overlap aaa or aa
            else:
                idx = self.find(subStr, start = (idx + length)) # allow or not overlap aaa or aa

        return count




    ## startswith
    def startswith(self, str, start = 0, end = -1):
        originalString = self.getString()

        if end == -1:
            end = len(originalString)

        if not self.__isqualified(str, start, end):
            return False
        
        if self.__findProcess(start, str) == -1:
            return False

        return True




    ## endswith
    def endswith(self, str, start = 0, end = -1):
        originalString = self.getString()

        if end == -1:
            end = len(originalString)

        if not self.__isqualified(str, start, end):
            return False

        end = end - (len(str) - 1)          # Start Point 
                                            # if char is 1 => len(originalString) - 1 
                                            # if char is more than 1 => len(originalString) - 1 - (len(char) - 1)
                                            # So, I need to subtract 1

        end -= 1                            # Settings => Because of Repeation Property

        ## checking
        if end - start < 0:            # size of str is bigger than the range.
            return False

        if self.__findProcess(end, str) == -1:
            return False

        return True




def main():
    text = "pypython python pyyy"
    o = "y"
    n = "java"
    str = myString(text)
    print(text.count(o))
    print(str.count(o))



main()