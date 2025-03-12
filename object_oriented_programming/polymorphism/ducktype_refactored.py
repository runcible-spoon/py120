class Wedding:
    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_wedding(self)

class Chef:
    def prepare_wedding(self, wedding):
        prepare_food(wedding.guests)

    def prepare_food(self, guests):
        # implementation

class Decorator:
    def prepare_wedding(self, wedding):
        decorate_place(wedding.flowers)

    def decorate_place(self, flowers):
        # implementation

class Musician:
    def prepare_wedding(self, wedding):
        prepare_performance(wedding.songs)

    def prepare_performance(self, songs):
        # implementation
