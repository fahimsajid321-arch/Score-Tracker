#OOPS Part 2
'''class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        Area = 3.14*self.radius**2
        return Area
    def perimeter(self):
        Perimeter = 2*3.14*self.radius
        return Perimeter
c1 = Circle(4)
print(c1.area())
print(c1.perimeter())'''

'''class Employee:
    def __init__(self,role,depart,salary):
        self.role = role
        self.depart = depart
        self.salary = salary

    def show_details1(self):
        print("Role =", self.role)
        print("Department =", self.depart)
        print("Salary =", self.salary)




class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Manger","IT","75,000")

    def show_details(self):
        print("Name =", self.name)
        print("Age =", self.age)
        print(self.show_details1())


e2 = Engineer("Faheem","26")
e2.show_details()'''






