#Given this class:

class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!

#One problem is that we need to keep track of different breeds of dogs, since they have slightly different behaviors.
#For example, bulldogs snore when they sleep, but other dogs do not.
#Okay, I have no idea if that's entirely true; I suspect it isn't. Let's pretend it is.

#Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

eli = Bulldog()
print(eli.sleep())
