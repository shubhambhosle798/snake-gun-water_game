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

    if (computer == you):
        print ("It's a draw")

    elif (computer == 1 and you == 2):
        print ("You Won!")

    elif (computer == 1 and you == 3):
        print ("You Lose!")

    elif (computer == 2 and you == 1):
        print ("You Lose!")

    elif (computer == 2 and you == 3):
        print ("You Won!")

    elif (computer == 3 and you == 1):
        print ("You Won!")

    elif (computer == 3 and you == 2):
        print ("You Lose!")

    else:
        print ("Something went wrong")

else:
    print ("This is invalid choice. Choose only between W, S, G")