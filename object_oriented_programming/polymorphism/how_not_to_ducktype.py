class Wedding:
    def prepare(self, preparers):
        for preparer in preparers:
            if preparer is Chef:
                preparer.prepare_food(guests)
            elif preparer is Decorator:
                preparer.decorarate_place(flowers)
            elif preparer is Musician:
                preparer.prepare_performance(songs)

class Chef:
    def prepare_food(self, guests):
        # implementation

class Decorator:
    def decorate_place(self, flowers):
        # implementation

class Musician:
    def prepare_performance(self, songs):
        # implementation
