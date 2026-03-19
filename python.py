# Aggregation = Represents a relationship where one object (the whole)
#               contains references to one or more INDEPENDENT objects (the parts)

#library is whole
#books are parts or independent objects

class Library:
    def __init__(self, name):
        self.name= name
        self.books=[]
    
    def add_books(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

        # for book in self.books:
        #     print(f"{book.title} by {book.author}")
        
#Book can exist without library and vice versa
class Book:
    def __init__(self, title, author):#constructor
        self.title= title
        self.author= author

library = Library("The Kathmandu Times Library")
book1 = Book("Matilda","Roald Dahl")
book2 = Book("Harry Potter","JK Rowling")

library.add_books(book1)
library.add_books(book2)

print(library.name)

for book in library.list_books():
    print(book)

# Composition= The composed object directly owns its components, 
#              which cannot exist independently "owns-a" relationship

class Engine:
    def __init__(self,horse_power):
        self.horse_power= horse_power

class Wheel:
    def __init__(self, size):
        self.size=size

class Car:
    def __init__(self,make, model, horse_power, wheel_size):
        self.make= make
        self.model= model
        self.engine= Engine(horse_power)
        self.wheels= [Wheel(wheel_size) for wheel in range(4)] 
    
    def display_cars(self):
        print(f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}")

car1= Car("BMW","X1",500,18)
car2= Car("Lamborghini","Revuelto",1001,20)

car1.display_cars()
car2.display_cars()

#Nested class = A class defined within another class
#          class Outer:
#                class Inner:
                         
"""Benefits :Allows you to logically group classes that are closely related
Encapsulates private details that aren't relevant outside of the outer class
Keeps the namespace clean; reduces the possibility of naming conflicts"""

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name= name
            self.position= position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name= company_name
        self.employees=[]

    def add_employees(self, name, position):
        new_employee= self.Employee(name,position)
        self.employees.append(new_employee)
        

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1= Company("Apple")
print(company1.company_name)


company1.add_employees("Steve Jobs","CEO")
company1.add_employees("Mark Zuckerberg","COO")
for employee in company1.list_employees():
    print(employee)

print("\n\n")
company2= Company("Tesla")
print(company2.company_name)

company2.add_employees("Kritartha","Manager")
company2.add_employees("Elon Musk","CEO")
for employee in company2.list_employees():
    print(employee)


    




        
        
        
