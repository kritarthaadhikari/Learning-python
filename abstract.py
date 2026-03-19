# Abstract class:
# A class that cannot be instantiated on its own; meant to be subclassed.
# They can contain abstract methods, which are declared but have no implementation.
# Abstract classes benefits:
# 1. Prevents-I instantiation of the class itself
# 2. Requires children to use inherited abstract methods
 
from abc import ABC, abstractmethod

#abc is a module, abstract base class
#ABC is a class inside abc module
class Vehicle(ABC):
    #parent class
    
    @abstractmethod #decorator
    def go(Self):
        pass

    @abstractmethod
    def stop(self):
        pass

#In abstract classes, we declare functions but don't define them

class Car(Vehicle):
    #sub class
    def go(self):
        print("You are driving the car")

    def stop(self):
        print("You stopped the car")

car= Car()
car.go()
car.stop()

#super() = Function used in a child class to call methods from a parent class (superclass).
#          Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius

        #Method Overriding can be done if i redeclare another function with the same name
    def describe(self):
        super().describe()
        print(f"It is a circle with the radius {self.radius} and area of {3.14*self.radius**2}")

class Square(Shape):
    def __init__(self, color, is_filled,width):
        super().__init__(color, is_filled)   
        self. width= width 

class Triangle(Shape):
    def __init__(self, color, is_filled,width,height):
        super().__init__(color, is_filled)  
        self.width= width
        self.height= height

circle= Circle("Black",True,5)
square= Square("Red",False,6)
triangle= Triangle("Blue",True, 6,5) 
circle.describe() 