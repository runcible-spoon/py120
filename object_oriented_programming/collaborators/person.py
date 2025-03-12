class Person:
    def __init__(self, my_name):
        self.my_name = my_name

    def name(self):
        return self.my_name

joe = Person("Joe")
print(joe.name()) # Joe
print(type(joe.name()) # <class 'str'>
