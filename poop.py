from car import car

car1= car("BMW",2025,"Black",False)
# print(car1)
# Address 

print(car1.model)
print(car1.year)

car2=car("Cheverlot",2026,"Red",True)
car3=car("Toyota",2020,"Black",False)

car1.drive()
car2.stop()
car3.describe_car()

# class variables = Shared among all instances of a class
                    # Defined outside the constructor
                    # Allow you to share data among all objects created from that class

class Student:

    class_year=2030 #class variable

    def __init__(self,name,age):
        self.name=name# independent Instance variable
        self.age=age
       # Student.num_of_students+=1  # ❌ Problem: num_of_students doesn't exist yet

# AttributeError: type object 'Student' has no attribute 'num_of_students'

Student1= Student("Kritartha",18)
Student2=Student("Pritam",17)
print(Student.num_of_students)
print(Student1.name)# independent instance variable
print(Student1.age)
print(Student.class_year) #More explicit to use the class name in the
#                          class variable rather than using instances of class
