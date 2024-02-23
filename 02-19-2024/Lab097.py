# Car -
# Object - Tesla, Lambo

class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

# self is a special veriable that is used within the context of OOP
# It is a referance to the instance of a class
# access and manupulate the attributes and methods of that instance / Object


def start_engine(self):
    print("Starting engine")

def drive(self):
    print("Drive")

def car_break(self):
    print("break")

def who_is_driving(self):
    print("I am driving  ->" + self.name)  # self is used for myself name

tesla_object_ref = Car()
lambo_object_ref = Car()

tesla_object_ref.name = "Tesla"  # Everyone has different attribute
lambo_object_ref.name = "lambo"

tesla_object_ref.who_is_driving()
lambo_object_ref.who_is_driving()