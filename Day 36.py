'''a = input("Enter your number:")
print("Multiplication Table of",a)
try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Invalid Input")
print("Some important line of code")
print("Program ended")'''

try:
    a = int(input("Enter Your Number:"))
    num=[2,3,4]
    print(num[a])
except ValueError:
    print("Incorrect Input")
except IndexError:
    print("Index Error")
