class Person:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name, persons=[]):
        self.name = name
        self.members = persons

    def __add__(self, other_team):
        if not isinstance(other_team, Team):
            return NotImplemented

        team_members = self.members + other_team.members
        return Team('Temporary Team', team_members)

    def __iadd__(self, other_team):
        if not isinstance(other_team, Team):
            return NotImplemented

        self.members += other_team.members
        return self

cowboys = Team(
    'Dallas Cowboys',
    [
        Person("Troy Aikman"),
        Person("Emmit Smith"),
        Person("Michael Irvin"),
    ]
)

niners = Team(
    'San Francisco 49ers',
    [
        Person("Joe Montana"),
        Person("Jerry Rice"),
        Person("Deion Sanders"),
    ]
)

dream_team = Team("Dream Team")
dream_team += cowboys
dream_team += niners

for person in dream_team.members:
    print(person.name)

# Troy Aikman
# Emmitt Smith
# Michael Iamervin
# Joe Montana
# Jerry Rice
# Deion Sanders


a = 1
a += 41 # Creates new int with value 42

b = [1, 2, 3]
b += [4, 5] # Mutates [1, 2, 3] to [1, 2, 3, 4, 5]
