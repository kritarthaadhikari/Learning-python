#while loops
name=input("Enter your name")
while name=="":
    print("You didn't enter your name")
    name=input("Enter your name")
print(f"Hello! {name}")

#
car=input("Enter the car you like(Enter z to quit)")
while not car=="z":
    print(f"You like {car}")
    car=input("Enter another car you like (Enter z to quit)")
print("thank you!")

#For loops
for x in range (1,11):#reversed means from 11 to 1, 11 exclusive,1 inclusive
    print("Happy new year!")
    print(x)
for x in name:
    print(x)
# for x in range(1,11,2): steps 2
#     print(x)

# for x in range(1,20):
#     if x==13:
#         continue
#     else:
#         print(x)

#Nested loop
for y in range(3):
    for x in range(1,11):
        while x%2==0:
         print(x,end=" ")#end="\n"  end=" "
         break
    print()    
    

