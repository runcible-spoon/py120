'''
Create a Person class with two instance variables to hold a person's first and last names.
The names should be passed to the constructor as arguments and stored separately.
The first and last names are required and must consist entirely of alphabetic characters.

The class should also have a getter method that returns the person's name as a full name (the first and last names are separated by spaces), with both first and last names capitalized correctly.

The class should also have a setter method that takes the name from a two-element tuple. These names must meet the requirements given for the constructor.

Yes, this class is somewhat contrived.

You can use the following code snippets to test your class. Since some tests cause exceptions, we've broken them into separate snippets.
'''

class Person:

    def __init__(self, first, last):

        self._first = first
        self._last = last

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first):

        if not first or not all([ char.isalpha() for char in first ]):
            raise TypeError("Name must be alphabetic.")

        self._first = first

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):

        if not last or not all([ char.isalpha() for char in last ]):
            raise TypeError("Name must be alphabetic.")

        self._last = last

    @property
    def name(self):
        return f'{self.first.title()} {self.last.title()}'

    @name.setter
    def name(self, name_tuple):

        self.first = name_tuple[0]
        self.last = name_tuple[1]


#Test snippet 1
actor = Person('Mark', 'Sinclair')
print(actor.name == 'Mark Sinclair')

actor.name = ('Vin', 'Diesel')
print(actor.name == 'Vin Diesel')

#actor.name = ('', 'Diesel') # ValueError: Name must be alphabetic.


#Test snippet 2
character = Person('annIE', 'HAll')
print(character.name == 'Annie Hall')
#character = Person('Da5id', 'Meier') # ValueError: Name must be alphabetic.

#Test snippet 3
friend = Person('Lynn', 'Blake')
print(friend.name == 'Lynn Blake')
#friend.name = ('Lynn', 'Blake-John') # ValueError: Name must be alphabetic.
