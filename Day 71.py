x = [1, 2, 3, 4]
print(dir(x)) #With this we get list of attributes and methods available for an object

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.num = 1

a = person("Faheem", 26)
print(a.__dict__) #It returns the dictonary representation of an object's attributes
print(help(person)) #To get help documentation for an object including description of its attributes and methods
print(help(a))