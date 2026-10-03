class Employee:
    company = "Apple"

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the company name is {self.company}")
    
    def changeCompanyName(cls, newCompany): #Now if we see with this way the company name will only be changes for the instance
        cls.company = newCompany
    @classmethod 
    def changeCompanyName(cls, newCompany): #Now here we used classmethod which will cause the change of company name in the class variable
        cls.company = newCompany

a = Employee()
a.name = "Faheem"
a.showDetails()
a.changeCompanyName("Google")
a.showDetails()
print(Employee.company) # here if we see the company name has remained the same but it was only changed for that specific instance