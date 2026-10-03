a = input("Enter a Number:")
if (a=="quit"):
    print("Correct Keyword")
elif(int(a)<5 or int(a)>9):
    raise ValueError("Wrong is input")
else:
    print("Run this")