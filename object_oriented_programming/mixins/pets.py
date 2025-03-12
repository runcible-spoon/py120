class Pet:
    def speak(self):
        pass

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

    def swim(self):
        return 'swimming!'

class Bulldog(Dog):
    def swim(self):
        return "can't swim!"

class Cat(Pet):
    def speak(self):
        return 'meow!'
