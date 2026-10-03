#Without Walrus Operator
# food = list()
# # inp = input("Enter your favourite food: ")
# while True:
#     inp = input("Enter your favourite food: ")
#     if inp == "quit":
#         break
#     food.append(inp)

# Now same code with walrus operator
foods = list()
while(food := input("Enter your favourite food: ") != "quit"):
    foods.append(food)