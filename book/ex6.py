'''
Add a class method to your Car class that calculates and prints any car's average gas mileage (miles per gallon).

You can compute the mileage by dividing the distance traveled (in miles) by the fuel burned (in gallons).
'''

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color

        self.speed = 0

        self.distance = 0
        self.fuel_burned = 0

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

    def spray_paint(self, color):
        if not isinstance(color, str):
            raise TypeError("Color must be a string.")

        self.color = color
        return f'Pssst. You spray paint the car {self.color}'

    @classmethod
    def get_mpg(self):
        return self.distance // self.fuel_burned

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
