class Employee:
    companyName = "Apple" #This is the Class Variable that is associated the the class and this will be same for each class
    noOfEmployees = 0 
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02 #This is the instance variable
        Employee.noOfEmployees = self.noOfEmployees + 1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raise_amount} in {self.companyName} and total Employees are {self.noOfEmployees}")

emp1 = Employee("Faheem")
emp1.raise_amount = 0.02
emp1.companyName = "Apple Pakistan" #Here as we know that the companyName was a class variable so it will only change for emp1 but it will remain same for that emp2
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)
# Employee.showDetails(emp1) 
emp2 = Employee("Awais")
emp2.companyName = "Samsung"
emp2.showDetails()