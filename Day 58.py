# class Person:
#     name = "Faheem"
#     occu = "Army"

#     def info(self):
#         print(f"{self.name},{self.occu}")

# a = Person()
# a.info()

class Person:
    #Contrustor
    def __init__(self, name, occu): 
        print("I am a person") #This statement will always execute whenever the object will be craeted in the person class
        self.name = name
        self.occu = occu

    def info(self):
        print(f"Name is {self.name} and occupation is {self.occu}")


a = Person("Faheem","Army")
b = Person("Waseem", "Trader")
c = Person(2 , 3)
a.info()
b.info()
c.info()