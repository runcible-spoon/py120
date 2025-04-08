class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age == other.age

    def __ne__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age != other.age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age < other.age

    def __le__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age <= other.age

    def __gt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age > other.age

    def __ge__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.age >= other.age

ted = Person('Ted', 33)
carol = Person('Carol', 49)

if ted < carol:
    print("Ted is younger than Carol")
else:
    print("Ted is older than Carol")

# TypeError: '<' not supported between instances of 'Person'
# and 'Person'
