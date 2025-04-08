class Person:
    pass

person1 = Person()
person2 = Person()
person3 = person2

print(hex(id(person1))) # 0x100339a90
print(hex(id(person2))) # 0x1002ef250
print(hex(id(person3))) # 0x1002ef250
print(person3 is person2) # True

my_str = 'hello!'

print(hex(id(my_str))) # 0x10038b300
