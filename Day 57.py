class Person:
    name = "Faheem"
    occupation = "Army"
    networth = 1000

    def info(self):
        print(f"My name is {self.name} and my occupation is {self.occupation} and my networth is {self.networth}")


a = Person()
print(a.name, a.networth, a.occupation)

b = Person()
b.name = "Waseem"
b.occupation = "Army"
b.networth = 2000

c = Person()
c.name = "Bilal"
c.occupation = "Army"
c.networth = 3000

a.info()
b.info()
c.info()

