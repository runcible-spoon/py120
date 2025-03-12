class SwimMixin:
    def swim(self):
        return 'swimming!'

class Pet:
    def speak(self):
        pass

    # run and jump methods moved to mammal class

class Mammal(Pet):
    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Fish(SwimMixin, Pet):
    pass

class Dog(SwimMixin, Mammal):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

    # swim method moved to SwimMixin

class Bulldog(Dog):
    def swim(self):
        return "can't swim!"

class Cat(Mammal):
    def speak(self):
        return 'meow!'
