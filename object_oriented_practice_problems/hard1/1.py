'''Question 1

Ben and Alyssa are working on a vehicle management system. So far, they have created classes called Auto and Motorcycle to represent
automobiles and motorcycles. After having noticed common information and calculations they were performing for each vehicle type,
they decided to break the common behaviors into a separate class called WheeledVehicle.
This is what their code looks like so far:
'''

class Vehicle:
    def __init__(self,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicle(Vehicle):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        super().__init__(kilometers_per_liter,
                         liters_of_fuel_capacity)
        self.tires = tire_list

    def tire_pressure(self, tire_index):
        self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

# Now Syl has asked them to incorporate a new type of vehicle into their system: a Catamaran, defined as follows:

class Catamaran(Vehicle):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(kilometers_per_liter,
                       liters_of_fuel_capacity)

        self._number_propellers = number_propellers
        self._number_hulls = number_hulls


'''
This new class does not fit well with the object hierarchy defined so far. Catamarans don't have tires.
But we still want a common code to track fuel efficiency and range.
Modify the class definitions and move code into a mix-in, as necessary, to share code among the Catamaran and the wheeled vehicles.
'''


auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0
