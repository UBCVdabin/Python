def GetPositives(listOfNums):
    pos = []
    for item in listOfNums:
        if item > 0:
            pos.append(item)

    return pos


def main():
    pos = GetPositives([-1, 0, 10, 20, -0.5, 0.5])
    print(pos)


    for i in range(len(pos)):
        print(pos[i])


main()