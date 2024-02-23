# Class & Object in Python
# Class - Attributes and Behaviour

# Person -> Objrct Vani, Pramod, Shreetam
# Methods are part of classes
# Functions are independent

class Person:
    # Attributes -> Data members
    name = None
    age = None
    id = None
    phone_no = None

    # Behaviour = Method ( Not the function )

    def talk (self):
        print("I can talk")

    def another():
        print(" I am a Function")

    def walk(self):
        return " I am walking"


def anotherf():
    print(" I am a f()")


# Objects - ClassName()
shreeram = Person()
shreeram.name = ("Shreeram")
print(shreeram.name)
shreeram.talk()   # This belong Shreeram
Pramod = Person()
amit = Person()

