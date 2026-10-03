class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1])) #here we did the same work but with the help of class method now we do not need to do it for each employee rather everytime whenever the input will be given in this form it will automatically split it.

e1 = Employee("Faheem", 12000)
print(e1.name)
print(e1.salary)

string = "Faheem-12000"
# e2 =Employee(string.split("-")[0], string.split("-")[1]) #Now if you have to do this, this is gonna make the work cumbersum and redundent for like 100 emplyees and it will make the code loook bad and for that we make classmethods and constructors
e2 = Employee.fromstr("Faheem-12000")
print(e2.name)
print(e2.salary)

# Another Exmaple
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split("-")
        return cls(name, int(age))
    
e3 = Person.from_string("Faheem-26")
print(e3.name)
print(e3.age)