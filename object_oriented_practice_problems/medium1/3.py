class Animal:
    def speak(self, words):
        print(words)

class Cat(Animal):
    def meow(self):
        self.speak('meow!')

class Dog(Animal):
    def bark(self):
        self.speak('woof! woof!')

cat = Cat()
cat.meow()

dog = Dog()
dog.bark()
