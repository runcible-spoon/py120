# Print the method resolution order for cars, trucks, boats, and vehicles as defined in the previous exercise.

class Vehicle:
    number_of_vehicles = 0

    def __init__(self):
        Vehicle.number_of_vehicles += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.number_of_vehicles

class SignalsMixin:

    def signal_left(self):
        print("Signalling left")

    def signal_right(self):
        print("Signalling right")

    def signal_off(self):
        print("Signal is now off.")

class Car(Vehicle, SignalsMixin):

    def __init__(self):
        super().__init__()

class Truck(Vehicle, SignalsMixin):

    def __init__(self):
        super().__init__()

class Boat(Vehicle):

    def __init__(self):
        super().__init__()


car1 = Car()
truck1 = Truck()
boat1 = Boat()

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
