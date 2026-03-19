#typecasting= The process of converting a value of one data type to another
# data type (string, integer , float,boolean)
#Explicit vs Implicit

name=input("Enter your name")
age=int(input("Enter your age"))
gpa=3.86
age+=1
print(age)

print(type(name))
print(type(age))
print(type(gpa))

age=float(age)
print(type(age))
name=bool(name)
print(name)
#if name variable is empty boolean shows false

#Implicit
x=2
y=2.0
x/=y
print(x)
#x was typecasted from int to float using simple arithmetic operations

#string methods
name="Kritartha"
print(type(str))
#result=len(str)
#position of a certain character(first occurence) 
result=name.find("r")
print(result)
   #result=1
result=name.rfind("t")
print(result)
   #Last occurence of the character
result=name.find("q")
print(result)
#result=-1 for no occurence of the character
#name=name.capitalize()
#name=name.upper()
#isdigit
result=name.isdecimal()
print(result)

#result=str.count("x") counts character
#result=str.replace("x","y") replaces x with y


