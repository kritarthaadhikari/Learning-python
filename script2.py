import script1
num1=2
num2=5
print("This is calculator")
print(f"The addition is {script1.add(num1,num2)}")
print(f"The subtraction is {script1.subtract(num1,num2)}")


"""
So maile k buje vanda kheri suppose i import
everything from script 1 to script 2 
and maile script 2 lai
run gare vane script 1 ko entire kura print hunxa
and if i don't want to run it directly
i use if_name_='_main_' esle garda kheri
chahi jj file ma xa tyo matra display hunxa
let us suppose script 1 ma from script2 export *
bahek kei xaina vane script 1 run garda
the code should be exited without errors 

output void
it's just like borrowing a function from another script
"""
# If _name_ == _main_: (this script can be imported OR run standalone)
#                      Functions and classes in this module can be reused
#                      without the main block of code executing

# ex. library = Import library for Functionality
#               When running library irectly, display a help page

