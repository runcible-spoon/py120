'''
Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car.

You should also add getter methods that let you view but not modify the car's model and year.

Don't forget to write some tests.
'''

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color

        self.speed = 0

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError("Color must be a string.")

        self._color = color

    def engine_on(self):
        return f"The {self.color} {self.year} {self.model}'s engine is on."

    def engine_off(self):
        self.speed = 0
        return f"Skrrt. The {self.color} {self.year} {self.model}'s speed is {self.speed} and its engine is off."

    def accelerate(self, number):
        self.speed += number
        return f'Vroom vroom. The {self.color} {self.year} {self.model} accelerated to {self.speed} miles per hour!'

    def decelerate(self, number):
        self.speed -= number
        return f'Skrrt. The {self.color} {self.year} {self.model} decelerated to {self.speed} miles per hour.'

    def current_speed(self):
        return f'Your speed is {self.speed}'

car = Car("Civic", "2016", "Black")


print(f"Car's model is {car.model}")
print(f"Car's model year is {car.year}")
print(f"Car's color is {car.color}")
car.color = "Blue"
print(f"Car's color is {car.color}")
car.color = 45
