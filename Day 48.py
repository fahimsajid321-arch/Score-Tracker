x = 5
print(x) #This will print value of x as 5

def Lvariable():
    global x
    x = 4
    print(x)

print(x) #This will print value of x as 5 because x is a global variable 
Lvariable() #This will pirnt value of x as 4 because that is the local function value of x
print(x) # Now because of global keyword value global value of x will be changed and after the function called once the global vlaue of x has updated