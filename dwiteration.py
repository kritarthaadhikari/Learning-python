# zip() = Combines multiple iterables (lists, tuples, sets, dict)
#             into a single iterator of tuples.
#             Makes managing multiple indices easier.
#             Returns a zip object

names = ["Spongebob", "Patrick", "Squidward"]
ages = [30, 35, 50]
jobs = ["Cook", "Unemployed", "Cashier"]

# for i in range(len(names)):
#     name= names[i]
#     age= ages[i]
#     job= jobs[i]
#     print(f"{name} is {age} years old and works as a {job}.")

data= zip(names, ages, jobs) #data is an object now, zip returns an object

#It can be turned into a list, tuple, set or dictionary using various funcs

for name, age, job in data:
    print(f"{name} is {age} years old and works as a {job}")


# recursion = a function that calls itself from within
#                      helps to visualize a complex problem into basic steps
#                      problems can be solved more easily iteratively or recursively
#                      iterative = faster, complex
#                      recursive = slower, simpler

#ITERATIVE
"""def walk(steps):
     for step in range(1,steps+1):
      print(f"You took step #{step}")

walk(100)"""

#RECURSIVE
"""def walk(steps):
    if steps==0:
        return
    walk(steps-1)
    print(f"You took step #{steps}")

walk(100)"""

#FACTORIAL

"""def factorial(num):
        factorial=1
        for x in range(1,num+1):
            factorial*=x
    return factorial
print(factorial(5))"""

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))

"""
The function keeps calling itself with steps-1 until steps becomes 0.
When steps == 0, it returns (stops recursion).
As each call finishes returning, the print() line runs,
so the steps are printed in order from 1 up to the number passed.
"""

# exception = An event that interrupts the flow of a program
#                     (ZeroDivisionError, TypeError, ValueError)
#                     1.try, 2.except, 3.finally
try:
    number = input("Enter a number")
    print(1/number)
except ZeroDivisionError:
    print("You foking idiot, you can't divide by 0")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something in the way!")
finally:
    print("Do some cleanup")
#finally always runs


