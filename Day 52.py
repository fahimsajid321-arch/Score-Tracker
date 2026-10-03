# def double(x):
#     return x*x


def appl(fx,value): #Here value can be any value and fx can be a small func given as an argument just like below
    return 6 + fx(value)

double = lambda x: x*x
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(double(2))
print(cube(2))
print(avg(2,3,4))
print(appl(lambda x: x*x*x,3)) #Here small func is being given as an argument to a bigger func
