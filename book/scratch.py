class GoodDog:

    def __init__(self, name):
        # self.name is an instance variable (state)
        self.name = name
        print(f'Constructor for {self.name}')

    # speak is an instance method (behavior)
    def speak(self):
        # we use the self.name instance variable
        print(f'{self.name} says Woof!')

    # roll_over is an instance method (behavior)
    def roll_over(self):
        # we're using the self.name instance variable
        print(f'{self.name} is rolling over.')

sparky = GoodDog('Sparky') # Constructor for Sparky
sparky.speak() # Sparky says Woof!
sparky.roll_over() # Sparky is rolling over.

rover = GoodDog('Rover') # Constructor for Rover
rover.speak() # Rover says Woof!
rover.roll_over() # Rover is rolling
