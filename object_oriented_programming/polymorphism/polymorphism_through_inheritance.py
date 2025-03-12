class Animal:
    def move(self):
        print(f"I am a {self.__class__.__name__}: I am not moving.")

class Fish(Animal):
    def move(self):
        print(f"I am a {self.__class__.__name__}: I am swimming.")

class Cat(Animal):
    def move(self):
        print(f"I am a {self.__class__.__name__}: I am walking.")

# Sponges and Corals don't have a separate move method - they don't move

class Sponge(Animal):
    pass

class Coral(Animal):
    pass

animals = [Fish(), Cat(), Sponge(), Coral()]
for animal in animals:
    animal.move()

#I am a Fish: I am swimming.
#I am a Cat: I am walking.
#I am a Sponge: I am not moving.
#I am a Coral: I am not moving.
