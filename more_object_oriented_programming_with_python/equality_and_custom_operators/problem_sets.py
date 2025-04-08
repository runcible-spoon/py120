class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def __add__(self, other):
        # if self is an integer
        if isinstance(self.value, int):
            if isinstance(other, int):
                sum_ = self.value + other
            elif other.isdigit():
                sum_ = self.value + int(other)
            else:
                sum_ = str(self.value) + other

        # if self is a numeric string
        elif self.value.isdigit():
            if isinstance(other, int):
                sum_ = int(self.value) + other
            elif other.isdigit():
                sum_ = int(self.value) + int(other)
            else:
                sum_ = self.value + str(other)

        # self is a non-numeric string
        else:
            sum_ = self.value + str(other)

        return f"Silly({sum_})"

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)
