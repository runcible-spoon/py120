class Dog:
    def walk(self):
        print("walkin the dog")

    def _chase_car(self):
        print("I'm chasin a car")

    def __goto_vet(self):
        print("The vet! Hide me!")

    def a_day_in_the_life(self):
        self.walk()
        self._chase_car()
        self.__goto_vet()

rover = Dog()

rover.a_day_in_the_life()   # walkin the dog
                            # I'm chasin a car
                            # The vet! Hide me!

rover.walk()                # walkin the dog
rover._chase_car()          # I'm chasin a car
rover._Dog__goto_vet()      # The vet! Hide me!
rover.__goto_vet()          # AttributeError: 'Dog' object has no attribute '__goto_vet'. Did you mean: '_Dog__goto_vet'?
