import random
import math
def throwDice():
    return random.randint(1, 6)

def FloatEqual(a, b, certainty = 0.0001):
    return math.fabs(a - b) < certainty

round = eval(input("How many round do you want to play?: "))

player_1 = 0
player_2 = 0
print()
for i in range(0, round):
    print("-----------------------------------------------")
    print("\t\t     Round " + str(i + 1))
    print("-----------------------------------------------\n\n")
    print("***********************************************")
    print("\t\tPlayer 1's Turn")
    print("***********************************************\n")
    input("Press enter to throw the Dice...\n")
    
    player_1 += throwDice()
    print("***********************************************")
    print("Player 1 has thrown the dice !")
    print("***********************************************\n\n")


    print("***********************************************")
    print("\t\tPlayer 2's Turn")
    print("***********************************************\n")
    input("Press enter to throw the Dice...\n")
    
    player_2 += throwDice()
    print("***********************************************")
    print("Player 2 has thrown the dice !")
    print("***********************************************")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


print("-----------------------------------------------")
print("\t\t     Result")
print("-----------------------------------------------")
print("Player 1's total score: " + str(player_1))
print("Player 2's total score: " + str(player_2))

avgOfplayer_1 = player_1 / round
avgOfplayer_2 = player_2 / round

print("Player 1's average score:", format(avgOfplayer_1, "<5.2f"))
print("Player 2's average score:", format(avgOfplayer_2, "<5.2f"))

if FloatEqual(avgOfplayer_1, avgOfplayer_2): 
    print("Result : " + "Draw !!" )
else:
    if avgOfplayer_1 > avgOfplayer_2:
        print("Result : " + "Player 1 Wins !!" )
    elif avgOfplayer_1 < avgOfplayer_2:
        print("Result : " + "Player 2 Wins !!" )
