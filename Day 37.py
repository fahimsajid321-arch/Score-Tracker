#Case 1
try:
    l = [2,3,4,5,6]
    x = int(input("Enter valid index:"))
    print(l[x])
except:
    print("Invalid Index")
print("Program closed")
#Case
try:
    l = [2,3,4,5,6]
    x = int(input("Enter valid index:"))
    print(l[x])
except:
    print("Invalid Index")
finally:
    print("Program closed")

#In case 1 and 2 program is performing same so we are unable to feel the use of "finally" but it is useful in case of funtion lets understad
#Case 3
def func1():
    try:
        l = [2,3,4,5,6]
        x = int(input("Enter valid index:"))
        print(l[x])
        return 0
    except:
        print("Invalid Index")
        return 1
    print("Program closed")

y = func1()
print(y)
#Case 4
def func1():
    try:
        l = [2,3,4,5,6]
        x = int(input("Enter valid index:"))
        print(l[x])
        return 0
    except:
        print("Invalid Index")
        return 1
    finally:
        print("Program closed")

y = func1()
print(y)
#See in case 3 and 4 when function is returning some value here in case 3 last print statement would never execute while in case 4 when we put that print in "finally" it will always execute no matter what so this is basically the use of "finally" and this is the example to understand the use of "finally".