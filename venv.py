# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB)(PRIORITY ORDER) Local - > Enclosed -> Global -> Built-in

# def func1():
#     a=1
#     print(a)#a is local to func1

#Enclosed
def func1():
    x=1

    def func2():
        print(x)
    func2()
func1()

#Global
def func1():
    print(x)

def func2():
    print(x)
x=1
func1()
func2()

from math import e
#in built   
def func1():
    print(e)

e=3
func1()





