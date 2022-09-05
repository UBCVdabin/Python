import random
import math 

number = random.randint(1,6)
print("The random number is " + str(number))

if math.sqrt(number) > 1.8:
    print("This number is Top half !")

else:
    print("This number is Bottom half !")
