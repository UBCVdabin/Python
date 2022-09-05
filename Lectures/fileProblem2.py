def GetData(fileName):
    ## returns the file content as a list of strings
    fileObject = open(fileName, "r")
    lst = fileObject.readlines()
    fileObject.close()
    return lst

def Clean(listOfStrings):
    for i in range(len(listOfStrings)):
        listOfStrings[i] = listOfStrings[i].strip()

def GetAirline(aString):
    res = aString.split(' ')
    name = res[0]
    stops = int(res[1])
    price = int(res[2])

    return name, stops, price

def GetAirlineList(sList):
    list = []

    for s in sList:
        name, stops, price = GetAirline(s)
        temp = [name, stops, price]
        list.append(temp)

    return list


def WriteData(lst, statue):
    ## outputs name and score of student (who got the highest) to fileName
    
    if statue == 1 or statue == 3:       ## Cheapest
        SelectionSort(lst, 1)

        if statue == 1:
            fileOb = open("cheapest.txt", 'w')
            fileOb.write(lst[0][0] + " " + str(lst[0][1]) + " " + str(lst[0][2]) + '\n')

        else:
            fileOb = open("SortedByPrice.txt", 'w')
            for i in range(len(lst)):
                fileOb.write (lst[i][0] + " " + str(lst[i][1]) + " " + str(lst[i][2]) + '\n')

    elif statue == 2 or statue == 4:    ## Order
        SelectionSort(lst, 2)

        if statue == 2:
            fileOb = open("leastStops.txt", 'w')
            fileOb.write(lst[0][0] + " " + str(lst[0][1]) + " " + str(lst[0][2]) + '\n')

        else:
            fileOb = open("SortedByStops.txt", 'w')
            for i in range(len(lst)):
                fileOb.write (lst[i][0] + " " + str(lst[i][1]) + " " + str(lst[i][2]) + '\n')

    fileOb.close()

def SelectionSort(aList, type):
    if type == 1:                                                           ## price
        for i in range (len(aList) - 1):
            for j in range (i+1, len(aList)):
                if aList[i][2] > aList[j][2]:
                    aList[i], aList[j] = aList[j], aList[i]


    else:                                                                   ## order
        for i in range (len(aList) - 1):
            for j in range (i+1, len(aList)):
                if aList[i][1] > aList[j][1]:
                    aList[i], aList[j] = aList[j], aList[i]


def main():
    list = GetData("flights.txt")
    # print(l)
    Clean(list)
    # print(l)
    AirlineList = GetAirlineList(list)
    print(AirlineList)

    WriteData(AirlineList, 1)
    WriteData(AirlineList, 2)
    WriteData(AirlineList, 3)
    WriteData(AirlineList, 4)

main()