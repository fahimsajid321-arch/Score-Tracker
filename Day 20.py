def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First Number is Greater")
    else:
        print("Second Number is Greater")

a = int(input("Enter the Number:"))
b = int(input("Enter the Number:"))
calculateGmean(a,b)
isGreater(a,b) 
