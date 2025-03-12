'''
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class.

The class should have at least one instance variable that gets initialized
by the initializer.

What class you create doesn't matter, provided it satisfies the above
requirements.
'''

class Vehicle:

    def __init__(self, name):
        self.name = name
        type_name = self.__class__.__name__
        print(f"This is a {name} of type {type_name}")

class Car(Vehicle):

    def operate(self):
        print(f'{self.name} drives.')

class Plane(Vehicle):

    def operate(self):
        print(f'{self.name} flies.')


lear = Plane('Learjet')
honda = Car('Honda Civic')

for vehicle in [lear, honda]:
    vehicle.operate()
