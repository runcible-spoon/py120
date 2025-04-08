class Vehicle:
    WHEELS = 4

    @classmethod
    def wheels(cls):
        return Vehicle.WHEELS

class Motorcycle(Vehicle):
    WHEELS = 2

    @classmethod
    def vehicle_wheels(cls):
        return cls.WHEELS

    @classmethod
    def motorcycle_wheels(cls):
        return Motorcycle.WHEELS

print(Motorcycle.wheels()) # 4
print(Motorcycle.WHEELS) # 2
print(Vehicle.wheels()) # 4
print(Vehicle.WHEELS) # 4
print(Motorcycle.vehicle_wheels()) # 2
