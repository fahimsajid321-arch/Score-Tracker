class Animal:
    def __init__(self, name1, specie):
        self.name1 = name1
        self.specie = specie

    def Show(self):
        print(f"The Name is {self.name1} and specie is {self.specie}")

class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
    def mammal_color(self):
        print(f"The name of Mammal is {self.name} and the fur color is {self.fur_color}")
class Dog(Animal,Mammal):
    def __init__(self, breed):
        Animal.__init__(self, "Dog", "Land Animal")
        Mammal.__init__(self, "Dogesh", "Brown")
        self.breed = breed
    def Sound(self):
        print("Barks")

d = Dog("German Shepard")
print(d.name1)
print(d.specie)
d.Show()
print(d.name)
print(d.fur_color)
print(d.breed)