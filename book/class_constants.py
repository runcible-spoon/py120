class GoodCat:
    CAT_YEARS = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human_age(self):
        return self.age * GoodCat.CAT_YEARS

cocoa = GoodCat('Cocoa', 4)
print(cocoa.human_age())
