def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

print(__name__)

if(__name__=="__main__"):
    print("Welcome to Calculator")
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))

    print(f"The addition of {num1} and {num2} is {add(num1,num2)}")
    print(f"The subtraction of {num1} and {num2} is {subtract(num1,num2)}")