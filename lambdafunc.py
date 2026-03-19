# Lambda function = A small anonymous function for a one time use (throw away function)
#                   They take any number of arguments, but have only 1 expression
#                   Helps keep the namespace clean and is useful with higher order functions
#                   'sort()', 'map()','filter(),'reduce() '
#                     lambda parameters: expression

double = lambda x:x^2 #expression =x^2
add= lambda x,y :x+y
max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
full_name = lambda first, last: first + " " + last
is_even = lambda x: x % 2 == 0
age_check = lambda age: True if age >= 18 else False

print(double(3))
print(add(3,4))
print(max_value(6, 7))
print(min_value(9, 8))
print(full_name("Spongebob", "Squarepants"))
print(is_even(5))
print(age_check(21))

# SORTING IN PYTHON .sort() or sorted()
# Lists[], Tuples(), Dictionaries{"":""}, Objects
#--------------Lists--------------------

fruits= ["banana","apple","orange","plum"]

fruits.reverse()#reverses 
#or fruits.sort(reverse=True)
print(fruits)
fruits.sort()
print(fruits)

#---------------Tuples---------------
fruits= ("banana","apple","orange","plum")
#Tuples have no attribute sort so we use the sorted ()

fruits= tuple(sorted(fruits,reverse=True)) #for reverse
#Sorted method converts tuple into a list

# fruits= sorted(fruits)
# fruits.reverse()
# fruits=tuple(fruits)
# print(fruits)

#-------------------Dictionary------------------
fruits= { "banana":125,
         "apple":200,
         "orange":300,
         "plum":500 }
fruits= dict(sorted(fruits.items()))
print(fruits)
# fruits= sorted(fruits.items())
# print(fruits)
#fruits.items turns key-value pair into a tuple 
#[('apple', 200), ('banana', 125), ('orange', 300), ('plum', 500)]

#for reverse 
fruits= dict(sorted(fruits.items(), key= lambda item: item[0],reverse=True))
print(fruits)

#item[0] represents the key and item[1] represents the value
"""for item in student.items():
    print("item:", item)
    print("item[0]:", item[0])  # key
    print("item[1]:", item[1])  # value
    print()

item: ('name', 'Kritartha')
item[0]: name
item[1]: Kritartha

item: ('age', 18)
item[0]: age
item[1]: 18

item: ('grade', 'A')
item[0]: grade
item[1]: A

"""
#For sorting in ascending and descending order of value
fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))


#------------------------Object-----------------------------
class Fruit:
   def __init__(self, name, calories):
       self.name = name
       self.calories = calories

   def __repr__(self):
       return f"{self.name}: {self.calories}"

fruits = [Fruit("banana", 105),
              Fruit("apple", 72),
              Fruit("orange", 73),
              Fruit("coconut", 354)]

# fruits = sorted(fruits, key=lambda fruit: fruit.name)
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# fruits = sorted(fruits, key=lambda fruit: fruit.calories)
# fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

print(fruits)
#so simply vanda yo sorted function ma chahi list paxi ko , key=....
# is the kura jasko basis ma we sort the object