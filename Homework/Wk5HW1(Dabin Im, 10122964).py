import math
import random
import sys
    

##Calculate Distance
def DistanceBetweenTwoPoints(x1, y1, x2, y2):
    dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return dist

##define the functions Throw and GetResult
def DiceThrow(player_name):

    result = random.randint(1, 6)
    print(player_name + " has thrown the dice.\n" + player_name + ": " + str(result) + "\n")
    return result

def GetResult(p1, p2):
    if p1 > p2:
        return 1
    elif p1 < p2:
        return 2
    else:
        return 0

def ShowTotalScore(player_name, score):
    print(player_name +"'s Score : " + str(score) + "\n")
                           
try:
    x1, y1 = eval(input("Enter Point A : "))
    x2, y2 = eval(input("Enter Point B : "))

    print("The distance between two points is " + str(DistanceBetweenTwoPoints(x1, y1, x2, y2)))


    ##game code
    ##player 1 throws twice
    player_1 = DiceThrow("player_1")
    player_1 = player_1 + DiceThrow("player_1")
    ShowTotalScore("player_1", player_1)

    ##Player 2 throws twice
    player_2 = DiceThrow("player_2")
    player_2 = player_2 + DiceThrow("player_2")
    ShowTotalScore("player_2", player_2)

    ##use GeResult(p1Total, p2Total) to find out the result
    result = GetResult(player_1, player_2)
    
    ##use the result to display appropriate message
    if result == 1:
        print("Player 1 wins !")
    elif result == 2:
        print("Player 2 wins !")
    else:
        print("Tie !")

except :
    print("Sorry... Error...")
    sys.exit(0)
    

