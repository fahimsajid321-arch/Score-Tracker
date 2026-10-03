#for loop with else statement
for i in range(5):
    print(i)
else:
    print("Loop terminated")
#for loop with break and else statement
for i in range(5):
    print(i)
    if(i==3):
        break       #here control will terminat the loop and else will also not execute
else:
    print("Loop terminated")
#while loop with else satement
j=0
while(j<10):
    print(j)
    j=j+1
else:
    print("Loop terminated")
#for loop with else
for x in range(5):
    print("Iteration no {} in for the loop".format(x+1)) #.format() is the method that is used for string interpolation 
else:
    print("else block in loop")

print("Out of the loop")