x = int(input("Enter your number:"))

match x:
    case 0:
        print("X is:",x)
    case 2:
        print("X is:",x)

    case _ if x!=90:
        print("X isn't 90")
    case _ if x!=80:
        print("X isn't 80")
    case _:
        print(x)