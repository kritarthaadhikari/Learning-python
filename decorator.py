# Decorator: A function that extends the behavior of another function
#            w/o modifying the base function
#            Pass the base function as an argument to the decorator
# @add_sprinkles
# get_ice_cream( "vanilla " )

def add_sprinkle(func):
    def wrapper(*args,**kwargs):
        print("*Sprinkles🎊 was added*")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("*Fudge🍫 was added*")
        func(*args,**kwargs)
    return wrapper
   
@add_sprinkle
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")

get_ice_cream("Chocolate")
#In case I don't use the wrapper function, the get_ice_cream function and the decorators work
#without being called 

# @property -Decorator used to define a method as a property (it can be accessed like an attribute)
#           Benefit: Add additional logic when read, write,or delete attributes
#           Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width= width
        self._height= height

    @property #getter methods
    def width(self):
        return f"{self._width:.1f} cm"
    
    @property #getter methods
    def height(self):
        return f"{self._height:.1f} cm" #private 
    
    @width.setter
    def width(self, new_width):
        if new_width>0:
            self._width= new_width

        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height>0:
            self._height= new_height

        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width is deleted")


rectangle= Rectangle(3,4)
print(rectangle.width)
print(rectangle.height)

rectangle.width= 7
print(rectangle.width)

del rectangle.width

