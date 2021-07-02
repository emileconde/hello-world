import converters
import utils
# the code below allows us the call the function without the class name
from converters import kg_to_lbs

# Importing from a different directory/package
import ecommerce.shipping
from ecommerce.shipping import calc_shipping

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")


    def draw(self):
        print("draw")


# point1 = Point()
# point1.x = 10    you can assign them attributes that are not defined in the class
# point1.y = 20
# print(point1.x)
# point1.draw()

point1 = Point(10, 20)
print(point1.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hey there! I am {self.name}")


john = Person("John")
john.talk()

# INHERITANCE
class Mammal:
    def wak(self):
        print("Walk")

# Inheriting from Mammal class
class Dog(Mammal):
    pass # python doesn't like empty classes so this is to just bypass


class Cat(Mammal):
    pass

dog = Dog()
dog.wak()

# IMPORTING FROM A DIFFERENT MODULE

print(converters.lbs_to_kg(300))

print(kg_to_lbs(135))

numborozoos = [23,45,56,7,9233]
print(utils.find_max(numborozoos))

calc_shipping()

