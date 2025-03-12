from color_mixin import ColorMixin

class Car(ColorMixin):

    def __init__(self, color):
        self.set_color(color)

car = Car('red')
print(car.get_color()) # red

car.set_color('green')
print(car.get_color()) # green

from color_mixin import ColorMixin

class SmartLight:

    def __init__(self, color):
        self.set_color(color)

smart_light = SmartLight('cool white')
print(smart_light.get_color()) # cool white

smart_light.set_color('goldenrod')
print(smart_light.get_color()) # goldenrod

from color_mixin import ColorMixin

class House:

    def __init__(self, color):
        self.set_color(color)

house = House('sky blue')
print(house.get_color()) # sky blue

house.set_color('lavender')
print(house.get_color()) # lavender
