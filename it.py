#Iterables= An object/collection that can return its
#           elements one at a time, allowing it to be iterated
# over in a loop



# Membership operators = used to test whether a value or variable is found in a sequence
# (string, list, tuple,set, or dictibnary)
#       1. in
#       2. not in


grades={"Kritartha":"A",
        "Sabal":"B",
        "Ujjwal":"A",
        "Prajesh":"B"}

student=input("Enter the name of a student")

if student in grades:
    print(f"{student}'s grade is {grades.get(student)}")
    #grades[student]
else:
    print(f"{student} was not found")

# Match-statement(switch): An alternative to using many 'elif' statements
# Execute some code if a value matches a 'case'
# Benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     match day:
#         case 1:
#             return "Sunday"
#         case 2:
#             return "Monday"
#         case 3:
#             return "Tuesday"
#         case 4:
#             return "Wednesday"
#         case 5:
#             return "Thursday"
#         case 6:
#             return "Friday"
#         case 7:
#             return "Saturday"
#         case _: #Wildcard _
#             return "Not valid"
        
# print(day_of_week(1))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
          return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
           return False
        case _:
            return False
        
print(is_weekend("Friday"))

# module: a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files
     
import math as m
from math import pi
print(pi)
print(m.pi)


    
    

         
    



