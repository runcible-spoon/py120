class GoodDog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f'{self._name} says arf!'

    def name(self):
        return self._name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self._name = new_name

    def age(self):
        return self._age

    def set_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError("Age must be an integer")
        if new_age < 0:
            raise ValueError("Age cannot be negative")
        self._age = new_age

sparky = GoodDog("Sparky", 5)

print(sparky.name()) # Sparky
print(sparky.age()) # 5

sparky.set_name("Fireplug")
print(sparky.name()) # Fireplug

sparky.set_age(6)
print(sparky.age()) # 6

sparky.set_name(42) # TypeError: Name must be a string
sparky.set_age(-1) # ValueError: Age cannot be negative
