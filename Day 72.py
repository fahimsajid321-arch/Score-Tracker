class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        self.laguage = lang
        super().__init__(name, id) #Here we are using the super method to get the attribute inherit from the parent class

a = Employee("Awais", 420)
print(a.name)
print(a.id)
b = Programmer("Faheem", 410, "Python")
print(b.name)
print(b.id)
print(b.laguage)
