class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
    def make_sound(self):
        print("Makes sound of an animal")

class Dog(Animal):
    def __init__(self, breed):
        Animal.__init__(self, "Dogesh", "Dog")
        self.breed = breed

    def make_sound(self):
        print("Barks")

class Cat(Animal):
    def __init__(self, Breed):
        super().__init__("Cato", "Cat")
        self.Breed = Breed

    def Catches(self):
        print("Catches Mouse")

d = Dog("German Shepard")
d.make_sound()
print(d.name)
print(d.breed)
print(d.specie)
c = Animal("Cato", "Cat")
c.make_sound() 
print(c.name)
print(c.specie)
a = Cat("Persian")
print(a.name)
print(a.specie)
a.make_sound()
a.Catches()
print(a.Breed)

