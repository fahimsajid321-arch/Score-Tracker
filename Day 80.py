class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
    def show_details(self):
        print(f"Name: {self.name}") #Here it will be executed first then it will go to the subsequent Show Details Class
        print(f"Specie: {self.specie}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, specie = "Dog")
        self.breed = breed
    def show_details(self):
        Animal.show_details(self) # From here it will go to the Show Details func of Animal Class
        print(f"Breed: {self.breed}")

class German_Shepard(Dog):
    def __init__(self, name, colour):
        Dog.__init__(self, name, breed= "German Shepard")
        self.colour = colour
    def show_details(self):
        Dog.show_details(self) # From here it went to the Show Details Func of Class Dog
        print(f"Colour: {self.colour}")

d = German_Shepard("Lucy", "Golden")
d.show_details() # Here when we called this it went to the Show_details func of Class German Shepard