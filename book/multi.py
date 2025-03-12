class Pet:

    def play(self):
        print("I am playing.")

class Predator:

    def hunt(self):
        print("I am hunting.")

class Cat(Pet, Predator):

    def purr(self):
        print("I am purring.")

cat = Cat()
cat.purr() # I am purring.
cat.play() # I am playing.
cat.hunt() # I am hunting.
