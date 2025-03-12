class MyClass:

    def __init__(self, x):
        self.x = x
        self.y = []
        self.z = 'xxx'


obj = MyClass(5)
print(obj.__dict__)
# {'x': 5, 'y': [], 'z': 'xxx'}
