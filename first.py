print("I like pizza")
#this is a comment and its my first python program
#String
first_name='Kritartha'
print(first_name)
print(f"hello {first_name}")

#Integers
age=18
print(f"Your age is {age}")

#Boolean
is_Student= True
if is_Student:
    print("You are a student")
else:
    print("You are not a student")
#Type Casting
#str(),int(),float(),bool()
name='Kritartha'
age=18
height=176.5
    
    
print(type(age))
height= int(height)
print(height)

name=""
#name="some value" else boolean rturns false
name=bool(name)
print(name)

#input() = A function that prompts the user to
# enter data. returns data as a string

name= input("What's your name?")
age= input("How old are you?")
age=int(age)
age+=1
height= int(input("Enter your height"))

print(f"My name is {name}")
print(f"Your age next year will be {age}") 

print(f"You are {height} cms tall")

#math functions
x=3.14
y=-200
z=20

print(round(x))
print(abs(y))
result=pow(abs(y),2)
print(result)
#max(x,y,z)


