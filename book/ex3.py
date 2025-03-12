'''
1. Create a `Car` class that meets these requirements:
    - Each Car object should have a model, model year, and color provided at instantiation time.
    - You should have an instance variable that keeps track of the current speed. Initialize it to `0` when you instantiate a new car.
    - Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
    - Create a method that prints a message about the car's current speed.
    - Write some code to test the methods.
'''

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def engine_on(self):
        print(f"The {self.color} {self.year} {self.model}'s engine is on.")

    def engine_off(self):
        self.speed = 0
        print(f"Skrrt. The {self.color} {self.year} {self.model}'s speed is {self.speed} and its engine is off.")

    def accelerate(self, number):
        self.speed += number
        print(f'Vroom vroom. The {self.color} {self.year} {self.model} accelerated to {self.speed} miles per hour!')

    def decelerate(self, number):
        self.speed -= number
        print(f'Skrrt. The {self.color} {self.year} {self.model} decelerated to {self.speed} miles per hour.')

    def current_speed(self):
        print(f'Your speed is {self.speed}')

car = Car("Civic", "2016", "Black")

car.engine_on()
car.current_speed()
car.accelerate(10)
car.current_speed()
car.decelerate(5)
car.current_speed()
car.engine_off()
