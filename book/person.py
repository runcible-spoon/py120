class Person:

    class _Name:

        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            return self.name == other.name

        def __ne__(self, other):
            return self.name != other.name


    def __init__(self, name1, name2):
        print(self._Name(name1) == self._Name(name2))

Person('John', 'John') # True
Person('Alice', 'Allison') # False
