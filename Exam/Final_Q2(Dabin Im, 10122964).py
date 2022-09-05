def Interlace(s1, s2):
    str = ""

    if len(s1) == 0 or len(s2) == 0:
        return str

    totalLength = len(s1) if len(s1) <= len(s2) else len(s2)

    for i in range(totalLength):
        str += s1[i]
        str += s2[i]

    return str

def main():
    print(Interlace("abc", "def")) #   returns "adbecf"
    print(Interlace("abc", "de"))  #   returns "adbe"
    print(Interlace("ab", "def"))  #   returns "adbe"
    print(Interlace("", "def"))    #   returns ""
    print(Interlace("abc", ""))    #   returns ""

main()