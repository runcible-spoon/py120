#Create a Car class that makes the following code work as indicated:

class Car:

    def __init__(self, id, year, color):
        self._id = id
        self._year = year
        self._color = color

        self.display_attributes(id, year, color)

    @property
    def id(self):
        return self._id

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    def display_attributes(self, id, year, color):
        return f'{self.color.title()} {self.year} {self.id}'

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.id)}, {self.year}, {repr(self.color)})'

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz == 'Red 2024 ID.Buzz')
print(repr(vwbuzz) == "Car('ID.Buzz', 2024, 'red')")
