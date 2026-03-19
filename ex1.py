# radius=float(input("Enter the radius of a circle"))

# area=3.1415*radius**2
# print(area)

# #in built functions; round(), abs(){absolute},pow(4,3):4**3, max(),min() 

#Weight Conversion
weight=float(input("Enter your wt"))
unit=input("enter the unit(kg or lbs)")

if(unit=="kg"):
    print("Weight in lbs is:")
    result=weight*2.205
    result=round(result,3)
    print(result)
elif unit=="lbs":
    print("Weight in kg is:")
    result=weight/2.205
    result=round(result,3)
    print(result)
else:
    print("Unit isnt valid")

"""logical operators
and, or , not
"""

# conditional expression= A one line shortcut for the if else statement (ternary operator)
#     print or assign one of two values based on a condition
# x if condition else Y

num=5
print("positive" if num>0 else "Negative")
#Positive

a=5
b=6
max_num=a if a>b else b
print(max_num)
#max_num=6=b

#Validate exercise
#1. usernameis no more than 12
#2. username must not contain spaces
#3. username must not contain digits

username=input("Enter your username")
if len(username)>12:
    print(f"Your username {username} contains more than 12 letters")
elif not username.find(" ")==-1: #returns -1 if no spaces
    print("Your username contains spaces")
elif not username.isalpha():
    print("Your username contains numbers")#gives bool as an output
