'''Question 7

What would happen if you ran the following code? Don't run it until you've checked your answer:
'''
class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model())
