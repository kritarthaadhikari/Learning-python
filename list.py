# collection =single "variable" used to store multiple values
# List = [ ] ordered and changeable. Duplicates 0K
# Set ={ } unordered and immutable, but Add/ Remove 0K. NO duplicates
# Tuple = ( ) ordered and unchangeable. Duplicates 0K. FASTER

#LIST
cars= ["BMW","Mercedez","Toyota","Tata"]
for car in cars:
    print(car)

print(cars[::-1])#print(cars)
# print(dir(cars)) {all the functions}
#to check whether a certain value is within the list

print("Tesla" in cars)

#cars.append("Tesla") {adds tesla into the list }
#cars.remove("Tesla")
#cars.insert(0,"pineapple")
#cars.clear() {clears the list}
#print(cars.index("BMW")) {prints the index of the value}
#cars.count("BMW") {counts the total number}
cars.sort()
print(cars)
cars.reverse()  
print(cars)


#SET
cars= {"BMW","Mercedez","Toyota","Tata"}

#List comprehension= A concise way to create listlS in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

# doubles=[]

# for x in range(1,11):
#     doubles.append(x**2)

# print(doubles)

doubles=[x**2 for x in range(1,11)]
print(doubles)

cars=["BMW","Toyota","Mercedez"]
cars=[car.upper() for car in cars]
print(cars)

numbers=[1,-2,-3,4,5,-6]
pos_num=[num for num in numbers if num>=0]

print(pos_num)