# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Vehicle: #Parent Class
    def __init__(self,name,wheels):
        self.name=name
        self.wheels= wheels

    def start(self):
        print(f"{self.name} is starting")

    def stop(self):
        print(f"{self.name} is stopping")

class Car(Vehicle): #child class
    def gears(self):
        print("5 gears")

class Scooter(Vehicle): #child class
    def gears(self):
        print("No gears")

car= Car("BMW",4)
car1= Car("Mercedez",4)

print(car.name)
car.start()

car1.gears()
scooty= Scooter("Fascino",2)
scooty.gears()

# multiple inheritance = inherit from more than one parent class
#                         C(A,B)
    
# multilevel inheritance= inherit from a parent which inherits from another parent
#        C(B)<- B(A)<- A

class Animal:

    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating")
class Prey(Animal):
  

    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Tiger(Predator):
    pass

class Fish(Prey,Predator): #Multiple Inheritance
    pass

rabbit= Rabbit("rabbit")
rabbit.flee()

fish= Fish("Shark")
fish.hunt()
fish.eat()

#Polymorphism = Greek word that means to "have many forms or faces"
# Poly = Many
# Morphe =Form
# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck typing"= Object must have necessary attributes/methods

from abc import ABC, abstractmethod
class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return 3.1415*self.radius**2

class Square(Shape):
    def __init__(self,width):
        self.width= width

    def area(self):
        return self.width**2

class Triangle(Shape):
    def __init__(self, height,base):
        self.height= height
        self.base= base
    
    def area(self):
        return 0.5*self.height*self.base

class Pizza(Circle): #Multi level Inheritance
    def __init__(self, topping,radius):
        super().__init__(radius)
        self.topping=topping
Shapes=[Circle(5),Square(5),Triangle(3,4),Pizza("Pepperoni",7)]

for shape in Shapes:
    print(shape.area())

# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must havq the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck. "


class Anime:
    exists=False

class Luffy(Anime):
    def punchline(self):
        print("Ore wa kaizoku-ō ni naru!")

class Ichigo(Anime):
    def punchline(Self):
        print("BANKAI! Tensa Zangetsu")

class Naruto(Anime):
    def punchline(Self):
        print("Dattebayo")

class Car:
    exists=True
    
    def punchline(Self):
        #car doesnt have a punchline but it makes noise so duck typing can be used
        # by altering the method name to minimum necessary attribute
        print("HONK!")

anime=[Luffy(),Ichigo(),Naruto(),Car()]

for ani in anime:
    print(ani.punchline())
    print(ani.exists)





