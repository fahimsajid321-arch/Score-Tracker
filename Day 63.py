import random
# user_input = int(input("Choose between 0 to 2:"))
# comp_input = random.randint(0,2)
# print("You Chose: ", user_input)
# print("computer Chose: ", comp_input)
def check():
    if (user_input == comp_input):
        return 0
    if (user_input == 1 and comp_input == 0):
        return -1
    if (user_input == 2 and comp_input == 1):
        return -1
    if (user_input == 0 and comp_input == 2):
        return -1
    else:
        return 1

User_List = []
Comp_List = []
for i in range (1,11):
    try:
        user_input = int(input("Choose between 0 to 2:"))
        if user_input not in (0,1,2):
            print("Invalid Input: Chose between 0 to 2")
            continue
    except ValueError:
        print("Please Enter Valid Integer")
        continue

    comp_input = random.randint(0,2)
    print("You Chose: ", user_input)
    print("computer Chose: ", comp_input)    
    score = check()
    print("Score of this game: ", score)
    if(score == 0):
        User_List.append(score)
        Comp_List.append(score)
        print("Your List of Games: ", User_List)
        print("Computer List of Games: ", Comp_List)
        print("Draw")
    elif(score == -1):
        User_List.append(-1)
        Comp_List.append(1)
        print("Your List of Games: ", User_List)
        print("Computer List of Games: ", Comp_List)
        print("Computer Wins")
    else:
        User_List.append(1)
        Comp_List.append(-1)
        print("Your List of Games: ", User_List)
        print("Computer List of Games: ", Comp_List)
        print("You win")
User_Total = sum(User_List)
Comp_Total = sum(Comp_List)
print("Your Total Score: ", User_Total)
print("Computer Total Score: ", Comp_Total)
if User_Total == Comp_Total:
    print("Draw")
elif User_Total > Comp_Total:
    print("You Won")
else:
    print("You Lose")

