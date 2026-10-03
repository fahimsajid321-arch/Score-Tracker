#PUBLIC ACCESS SPECIFIERS EXAMPLE
# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    
#     def employee(self):
#         print(self.name)
#         print(self.age)

# a = Employee("Faheem", 26)
# a.employee()

# PRIVATE ACCESS SPECIFIER EXAMPLE
# class Employee:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
    
#     def employee(self):
#         print(f"Name is {self.__name} and age is {self.__age}") 

# a = Employee("Faheem", 26)
# print(a.__name) this will give error because of private attribute
# print(a._Employee__age)
# print(a._Employee__name)
# a.employee()

#PROTECTED ACCESS SPECIFIER EXMAPLE
class Student:
    def __init__(self):
        self._name = "Faheem"

    def _MyFun(self):
        return "Faheem will be good programmer"

class Subject(Student):
    #Inheritance
    pass

obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._MyFun())
print(obj1._name)
print(obj1._MyFun)


    

