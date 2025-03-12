class Shape:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def area(self):
        my_area = self._width * self._height
        print(f'area is {my_area}')

class Rectangle:

    def __init__(self, width, height):
        self._shape = Shape(width, height)

    def set_width(self, width):
        self._shape.set_size(width, self._shape.height)

    def set_height(self, height):
        self._shape.set_size(self._shape.width, height)

    def area(self):
        self._shape.area()

class Square(Shape):

    def __init__(self, size):
        self._shape = Shape(size, size)

    def set_size(self, size):
        self._shape.set_size(size, size)

    def area(self):
        self._shape.area()
