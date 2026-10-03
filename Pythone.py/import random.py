import random
target = random.randint(1,1000)
while True:
    userChoice = input("Guess the target or Quit :")
    if (userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Cogratulations : You Won")
        break

    elif(userChoice < target):
        print("Make a bigger choice")
    else:
        print("Make a lesser guess") 

print ("Game Over")
