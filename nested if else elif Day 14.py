num = int(input("Enter Your Number:"))
if(num>0):
    if(num>0 and num<=10):
        print("Number is between 0 to 10:",num)
    elif(num>10 and num<=20):
        print("Number is between 11 to 20:",num)
    elif(num>20):
        print("Number is greater than 20:",num)
    else:
        print("Invalid Number")
else:
    if(num<0 and num>=-10):
        print("Number is between 0 to -10:",num)
    elif(num<-10 and num>=-20):
        print("Number is between -11 to -20:",num)
    elif(num<-20):
        print("Number is less than -20:",num)
    else:
        print("Number is zero")

print("Program has been completed")