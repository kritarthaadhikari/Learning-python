# print("I love Pizza")
# string, integer, boolean,float

# This is a comment
# that spans multiple
# lines in Python
# print("Hello World")

# """
# This is a multi-line "comment".
# Technically, it's a string literal,
# but Python will ignore it if it's not used.
# """


# """
# String 
# first_name= "Kritartha"
# print(first_name)
# print(f"Hello {first_name}")

# Integer
# age=25
# print(f"You are {age} years old")
# qty=2
# print(f"iI'm buying {qty} bags")

# Float
# price=25.9
# print(f"The price of new bag is ${price}")

# Boolean
# is_student=True
# if is_student:
#     print("yes is a student")
# else:
#     print("you are not a student")
#     """

Name= "kritartha"
age=25
is_student= True
if is_student:
    print(f"Name:{Name} age{age}")

else:
    print("Invalid")


if age<=18:
    print("You can access this")
elif age>=100:
    print("Retire fella")
else:
    print("You cant access this")

    #elif

response=input("Do you want some food?(Y/N)")
if response=="Y":
    print("Have some food!")
else:
    print("You cant have food!")

name=""
name=bool(name)
print(name)
if name==False:
    print("Enter your name please!")
else:
    print("Thank you")
