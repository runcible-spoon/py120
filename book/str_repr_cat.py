class Cat:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name != other.name

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name < other.name

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name <= other.name

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name < other.name

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name >= other.name

fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')
whiskers = Cat('Whiskers')

print(fluffy < whiskers) # True
print(fluffy <= whiskers) # True
print(fluffy <= fluffy2) # True
print(fluffy > whiskers) # False
print(fluffy >= whiskers) # False
print(fluffy >= fluffy2) # True
