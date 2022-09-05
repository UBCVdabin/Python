import random
import math

##define the functions Throw and GetResult
def DiceThrow(player_name):

    result = random.randint(1, 6)
    DesignGameScreen()
    print(player_name + " has thrown the dice.\n" + player_name + ": " + str(result))
    return result

def FloatEqual(a, b, certainty = 0.0001):
    return math.fabs(a - b) < certainty

def ShowTotalScore(player_name, score):
    print(player_name +"'s Score: " + str(score) + "\n")

def DesignGameScreen(count= 45, lines= 1, char= '-'):
    for i in range(0, count):
        print(char, end = "")

    for i in range(0, lines):
        print()
    
def ShowResult(player_1, player_2, round):
    avgOfplayer_1 = player_1 / round
    avgOfplayer_2 = player_2 / round

    print("Player 1's average score:", format(avgOfplayer_1, "<5.2f"))
    DesignGameScreen(count=0)
    print("Player 2's average score:", format(avgOfplayer_2, "<5.2f"))
    DesignGameScreen(count=0, lines=2)

    if FloatEqual(avgOfplayer_1, avgOfplayer_2): 
        print("Result : Draw !!" )
    else:
        if avgOfplayer_1 > avgOfplayer_2:
            print("Result : Player 1 Wins !!" )
        else:
            print("Result : Player 2 Wins !!" )

    DesignGameScreen(count=0)
                           
try:
    round = eval(input("How many rounds do you want to play?: "))
    DesignGameScreen(count=0)
    player_1 = 0
    player_2 = 0
    ##game code

    for i in range(0, round):
        DesignGameScreen()
        DesignGameScreen(char=" ")
        print("\t\t    Round " + str(i + 1))
        DesignGameScreen(char=" ")
        DesignGameScreen(lines= 3)

        DesignGameScreen(char='*')
        print("*                                           *")
        print("*              Player 1's TURN              *")
        print("*                                           *")
        DesignGameScreen(char='*')
        input("Press enter to throw the Dice...\n\n")

        ##player 1 throws twice
        player_1 += DiceThrow("player_1")

        DesignGameScreen(lines= 5)
        DesignGameScreen(char='*')
        print("*                                           *")
        print("*              Player 2's TURN              *")
        print("*                                           *")
        DesignGameScreen(char='*')
        input("Press enter to throw the Dice...\n\n")

        ##Player 2 throws twice
        player_2 += DiceThrow("player_2")
        DesignGameScreen(lines= 20)

    DesignGameScreen(char='*')
    print("*                                           *")
    print("**                  Result                 **")
    print("*                                           *")
    DesignGameScreen(char='*')

    ShowTotalScore("player_1", player_1)
    ShowTotalScore("player_2", player_2)

    ShowResult(player_1, player_2, round)

    input("Press an enter to finish the console")


except :
    print("Sorry... Error...")
    sys.exit(0)
    
