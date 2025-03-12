class Person:
    def __init__(self):
        self._heroes = ['Superman', 'Spiderman', 'Batman']
        self.cash = {
            1:      12, # denomination, count
            2:      1,
            5:      2,
            10:     3,
            20:     2,
            50:     1,
            100:    1,
        }

    def cash_on_hand(self):
        return sum([denomination * count for denomination, count in self.cash.items()])

    def heroes(self):
        return ', '.join(self._heroes)

joe = Person()
print(joe.cash_on_hand()) # 244
print(joe.heroes()) # Superman, Spiderman, Batman
