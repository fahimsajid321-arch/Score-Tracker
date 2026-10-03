#factorial 5 = 5*4*3*2*1
#and by default Factorial 0 = 1

'''def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        print(n * factorial(n-1))   #this is wrong because function need to return the value back to the function so basically instead
                                     of print we need to use return statment here 

factorial(5)'''



def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1) #this is the correct way because it will return the value back to function
    
print(factorial(4))


#Fabonacci sequence code
def fabonacci_seq(m):
    if(m==0):
        return 0
    elif(m==1):
        return 1
    else:
        return fabonacci_seq(m-1) + fabonacci_seq(m-2)
    
print(fabonacci_seq(6))


d = int(input("Enter a number:"))
fb=0
for i in range(d+1):
    
    fb = fb + i

print(fb)
