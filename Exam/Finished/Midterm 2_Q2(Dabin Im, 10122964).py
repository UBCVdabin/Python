import random

##define the functions Throw and GetResult
def Throw(n):
    highestScore = 0

    for i in range(0, n):
        result = random.randint(1, 6)
        
        if highestScore < result:
            highestScore = result

    return highestScore

def DesignGameScreen(count= 64, lines= 1, char= '='):
    for i in range(0, count):
        print(char, end = "")

    for i in range(0, lines):
        print()

def ShowResult(Attacker, Defender):
    if Attacker > Defender:
        print("Attacker has won the battle" )
    elif Attacker < Defender:
        print("Defender has won the battle")
    else:
        print("THEY ARE A TIE")

def ShowRoundResult(winner_player, defeat_player):
    print(winner_player + " is successful. " + defeat_player + " loses a soldier")

                        
def PlayGame(n):
    Attacker = 5
    Defender = 5
    resultOfAttacker = 0
    resultOfDefender = 0

    for i in range(0, n):
        if Attacker == 0 or Defender == 0:
            break

        DesignGameScreen()
        print("Round: " + str(i + 1))
        print("Attacker has " + str(Attacker) + " soldiers.")
        print("Defender has " + str(Defender) + " soldiers.")
        resultOfAttacker = Throw(3)
        print("Attacker threw: " + str(resultOfAttacker))
        resultOfDefender = Throw(2)
        print("Defender threw: " + str(resultOfDefender))

        if resultOfAttacker > resultOfDefender:
            ShowRoundResult("Attacker", "Defender")
            Defender -= 1
        else:
            ShowRoundResult("Defender", "Attacker")
            Attacker -= 1

        DesignGameScreen()

    DesignGameScreen()
    print("FINAL RESULT")
    DesignGameScreen()
    ShowResult(Attacker, Defender)

    input("\nPress an enter to finish the console")


def main():
    round = eval(input("How many rounds do you want to play?: "))
    PlayGame(round)
    

main()
