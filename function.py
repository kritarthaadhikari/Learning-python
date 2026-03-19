# #function = A block of reusable block of codes
# #           place () after the function name to invoke it

# def christmas(name):
#     print(f"Merry Christmas {name}\n")

# christmas("Kritartha")
# christmas("Kritika")

# #return = statement used to end a function
# #         and send a result back to the caller

# def add(x,y):
#     z=x+y
#     return z

# def subtract(x,y):
#     z=x-y
#     return z

# def multiply(x,y):
#     z=x*y
#     return z

# def divide(x,y):
#     z=x/y
#     return z

# print(add(2,3))
# print(subtract(4,3))
# print(divide(3,1))
# print(multiply(3,2))

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    full_name= first + " " + last
    return full_name

fN=input("Enter your first name")
lN=input("Enter your last name")
print(create_name(fN,lN))

#default arguments= A default value for certain parameters default
#                   is used when that argument is omitted make your 
#                   functions more flexible, reduces # of arguents
# 1. positional, 2. default, 3.keyword, 4.arbitrary

def net_price(list_price, discount=0,tax=0.05):
    return list_price*(1-discount)*(1+tax)

# print(net_price(500))
# print(net_price(500,0.1,0))
# print(net_price(500,0.1))

import time
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")
print(count(1))

#keyword arguments = an argument preceeded by an identifier
#                    helps with readability
#                    order of arguments doesn't matter

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num=get_phone(country=977, first=244, area=986, last=1300)
print(phone_num)

#*args= allows you to pass multiple non key arguments
# **kwargs(kw- keyword , args= arguments)= allows you to pass multiple keyword -arguments
# *unpacking operator

# def add(*nums):
#     total=0
#     for x in nums:
#         total+=x
#     return total

# print(add(1,2,3,4,5,6))

def name(*names):
    for name in names:
        print(name, end=" ")
    print()

name("Er.","Kritartha","Adhikari","I")

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}={value}")

print_address(city="KTM"
              ,province="Bagmati",
              municipality="Gokarneshwor")

#Arbitrary 
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('district')} {kwargs.get('province')} {kwargs.get('municipality')}")
    
shipping_label("Er.","Kritartha","Adhikari",district="Kathmandu",
               province="Bagmati"
               ,municipality="Gokarneshwor")






