class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

cat = Cat('tabby')
cat2 = Cat('orange')
cat3 = Cat('tuxedo')
print(Cat.cats_count())
