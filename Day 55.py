import random
snake = -1
water = 0
gun = 1
yourchoice = int(input("Enter your choice(-1,0,1): "))
if yourchoice not in [-1, 0, 1]:
    raise ValueError("Incorrect Input")
options = [-1, 0, 1]
computer_choice = random.choice(options)
print(computer_choice)
if yourchoice == -1 and computer_choice == options[0]:
    print("Draw")
elif yourchoice == -1 and computer_choice == options[1]:
    print("Win")
elif yourchoice == -1 and computer_choice == options[2]:
    print("Lose")
elif yourchoice == 0 and computer_choice == options[0]:
    print("Lose")
elif yourchoice == 0 and computer_choice == options[1]:
    print("Draw")
elif yourchoice == 0 and computer_choice == options[2]:
    print("Win")
elif yourchoice == 1 and computer_choice == options[0]:
    print("Win")
elif yourchoice == 1 and computer_choice == options[1]:
    print("Lose")
else:
    print("Draw")
