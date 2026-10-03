'''class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in the database..")

s1 = Student("Faheem Sajid")
print(s1.name)'''

'''class Car:
    color = "Blue"
    Brand = "Mercedes"

car1 = Car()
print(car1.color, end=" ")
print(car1.Brand)'''

'''class Student:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("Hello", self.name)

s1 = Student("Faheem")
s1.hello()'''

#Practice Question
'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print(self.name, "Your Marks Are", sum/3)

s1 = Student("Faheem", [99,98,97])
s1.average()

s1.name = "Faheem Sajid"
s1.average()'''

'''class Account:
    def __init__(self, acc_num, bal):
        self.account_num = acc_num
        self.balance = bal

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs.", amount, "deducted and your new balance is", self.balance)
        print("New Balace is", self.get_bal())

    def credit(self, amount):
        self.balance= self.balance + amount
        print("Rs.", amount, "was credit and your new balance is", self.balance)
        print("New Balace is", self.get_bal())

    def get_bal(self):
        return self.balance


        

acc1 = Account(12345,9000)
acc2 = Account(54321,18000)
acc1.debit(2000)
acc1.credit(5000)

acc2.debit(5000)
acc2.credit(10000)'''

class Person:
    __name = "Faheem Sajid"

    def __hello(self):
        print("Hello", self.__name)

    def welcome(self):
       self.__hello()

P1 = Person()
P1.welcome()


