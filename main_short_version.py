'''
1 = Snake = s
2 = Gun = g
3 = Water = w
'''

import random

print ("Before starting! \nUnderstand that, S means Snake, G means Gun, W means Water")

computer = random.choice([1, 2, 3])
yourChoice = input("Enter your choice between S, G, W: ").lower()

Dict = {"s" : 1, "g" : 2, "w" : 3}
reverseDict = {1 : "Snake", 2 : "Gun", 3 : "Water"}

if((yourChoice == "w") or (yourChoice == "s") or (yourChoice == "g")):
    you = Dict[yourChoice]

    print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")  # printing the choice of both sides

    if((computer - you) == 1 or  (computer - you) == 2):
        print("You Lose!")

    elif((you - computer) == -1 or (you - computer) == -2):
        print("You Lose!")

    elif (computer == you):
        print ("It's a draw")

    else:
        print("You Won!")

else:
    print ("This is invalid choice. Choose only between W, S, G")