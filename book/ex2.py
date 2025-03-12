# Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.

class Foo:

    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am a {type_name} object')

        type_name = self.__class__.__name__
        print(f"Here's another way of saying: I am a {type_name} object")


foo_instance = Foo('foo instance')
