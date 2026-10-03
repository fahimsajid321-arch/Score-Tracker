class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The Name of Employee is {self.name} and ID is {self.id}")

class Programmer(Employee):
    def Language(self):
     print("Pythone Developer")

e1 = Employee("Awais", 450)
e1.showDetails()
e2 = Programmer("Faheem", 550)
e1.showDetails()
e2.Language()