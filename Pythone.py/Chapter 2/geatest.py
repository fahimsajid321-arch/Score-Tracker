num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))

if(num1>num2 and num1>num3):
    print("num1 is greatest")
elif(num2>num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")
