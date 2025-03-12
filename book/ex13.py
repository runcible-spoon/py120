# Create a mix-in for the `Car` and `Truck` classes from the previous exercise that lets you operate the turn signals: signal left, signal right, and signal off. Use the following code to test your code.

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

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'
