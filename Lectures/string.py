## "adam", "mark", "mary"
#import re

#class Person():
#    def __init__(self, name):
#        self.name = name

#    def __str__(self):
#        s = self.name
#        return s


#def compareAlpabet(p_name1, p_name2):
#    if p_name1 > p_name2:
#        return True

#    else:
#        return False

        


#def main():
#    adam = Person("adam")
#    mark = Person("mark")
#    mary = Person("mary")

#    people = []

#    people.append(mary)
#    people.append(mark)
#    people.append(adam)

#    for i in range(len(people) - 1):
#        for j in range(i + 1, len(people)):
#            if(compareAlpabet(people[i].name, people[j].name)):
#                temp = people[i] 
#                people[i] = people[j]
#                people[j] = temp

#    for i in range(len(people)):
#        print(people[i].name)

#main()

##import random

##def makePassword():
##    pw = ""
##    for i in range(5):
##        pw += throwAlpabet()
##    return pw


##def throwAlpabet():
##    a = random.randint(97, 122)
##    return chr(a)


##s = makePassword()
##print(s)


#s = "abcdefg"

#print(len(s))

#print(s[3])

#print(s[len(s) - 1])

#print(s[-1:-4:-1])

###strings are immutable
## s[3] = "k" ## NOT ALLOWED
### cannot modify (mutate) an existing string

###create a new string with modifications
#newS = ""
#newS = s[:3] + "k" + s[4:]


#x = "abcd123"

#print(x.isdigit())

#def MyIsDigit(string):
#    '''
#    returns true if every character is
#    a digit, false otherwise.
#    There must be at least 1 character.
#    '''
#    if len(string) < 1:
#        return False

#    ## a for loop that goes through 
#    # all characters by position
#    for i in range(len(string)):
#        aChar = string[i]
#        if not (aChar >= '0' and aChar <= '9'):
#            return False
    
#    return True


###test cases
#print(MyIsDigit(x)) ## outputs False


#def MyIsDigit(string):

#    string = string.strip()

#    if len(string) < 1:
#        return False

#    for s in string:
#        if not(ord(s) >= 48 and ord(s) <= 57):
#            return False

#    return True
  

