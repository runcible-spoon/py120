class Foo1:

    @classmethod
    def bar(cls):
        print("this is bar in Foo1")

    def qux(self):
        type(self).bar() # type(obj) as the caller -- fine
        self.__class__.bar() # obj.__class__ as the caller -- most readable
        self.bar() # self inside a method
        Foo1.bar() # obj as the caller -- strongly discouraged

class Foo2(Foo1):

    @classmethod
    def bar(cls):
        print("this is bar in Foo2")

foo1 = Foo1()
foo1.qux()

'''
this is bar in Foo1
this is bar in Foo1
this is bar in Foo1
this is bar in Foo1
'''

foo2 = Foo2()
foo2.qux()

'''
this is bar in Foo2
this is bar in Foo2
this is bar in Foo2
this is bar in Foo1
'''
