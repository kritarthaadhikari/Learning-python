# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions
              
# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
#Class methods= Best for class-level data or require access to the class itself

class Employee:
    def __init__(self,name, position):
        self.name= name
        self.position= position

    def get_info(self):
        return f"{self.name}={self.position}"
    #Instance methods ^
    
    @staticmethod
    def is_valid_positions(position):
        valid_positions= ["Manager","Cook","Janitor","Waiter"]
        return position in valid_positions
    
#Static methods don't need objects to be defined like
#employee1=Employee(sdjsdhbsakjbdckj)
#you only need to access class

employee1= Employee("Kritartha","Manager")
employee2= Employee("Prajesh","Waiter")
employee3= Employee("Sabal","Janitor")
employee4= Employee("Ujjwal","Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())

print(Employee.is_valid_positions("Cook"))

class Student:
    count=0
    total_gpa=0
    def __init__(self, name, gpa):
        Student.count+=1
        self.name= name
        self.gpa= gpa
        Student.total_gpa+= gpa
    
    #Instance Method
    def get_info(self):
        return f"{self.name}={self.gpa}"
    
    @classmethod

    def get_count(cls):
        return f"The # of students is {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        return f"{cls.total_gpa/cls.count}"
    
std1= Student("Kritartha",4)
std2= Student("Prajesh",3.9)
print(Student.get_count())
print(Student.get_average_gpa())

class Employee:
    company_name = "TechCorp"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}, {self.age} years old, works at {Employee.company_name}"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def is_adult(age):
        return age >= 18


# Create employees
emp1 = Employee("Alice", 25)
emp2 = Employee("Bob", 17)

# Use instance method
print(emp1.get_info())
print(emp2.get_info())

# ✅ Use static method with instance data
print(Employee.is_adult(emp1.age))  # same as Employee.is_adult(25)
print(Employee.is_adult(emp2.age))  # same as Employee.is_adult(17)

# Change company name using class method
Employee.change_company("OpenAI")

# See the updated info
print(emp1.get_info())
print(emp2.get_info())

#Output
# Alice, 25 years old, works at TechCorp
# Bob, 17 years old, works at TechCorp
# True
# False
# Alice, 25 years old, works at OpenAI
# Bob, 17 years old, works at OpenAI

#Magic methods= Dunder methods __init__,__str__,__eq__
#               They are automatically called by many of Python's built in 
#               operations.They allow developers to define or customize
#               the behavior of objects.

class Book:
    def __init__(self,title, author, num_pages):
        self.title= title  
        self.author= author
        self.num_pages= num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other): #dunder equals
        return self.title == other.title and self.author== other.author
    
    def __lt__(self,other): #less than 
        return self.num_pages <other.num_pages
        
    def _gt__(self,other): #greater than
        return self.num_pages > other.num_pages

    def __add__(self,other):
        return f"{self.num_pages+ other.num_pages}pages"
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key=="title":
            return self.title
        elif key=="author":
            return self.author
        elif key=="num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"
            
book1= Book("The Hobbit","JRR Tolkein",310)
book2= Book("Matilda","Roald Dahl",290)
book3= Book("The Hobbit","JRR Tolkein",239)
print(book1)
print(book2)
print(book1==book2)
print(book1==book3)
print(book1>book2)
print(book2<book3)
print(book1+book2)
print("Dahl" in book2)
print(book1.title)
print(book1["title"])
print(book3["num_pages"])



