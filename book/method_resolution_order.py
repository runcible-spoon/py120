class LandDwellingMixin:
    pass

class LanguageMixin:
    pass

class BipedalismMixin:
    pass

class Creature:
    pass

class Mammal(Creature):
    pass

class Primate(LandDwellingMixin, Mammal):
    pass

class Human(BipedalismMixin, LanguageMixin, Primate):
    pass

print(Human.mro())
