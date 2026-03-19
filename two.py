#2D Array
fruits=["apple","Orange","Banana"]
vegetable=["Cauli","brocoli"]
meats=["mutton","chicken"]

groceries=[fruits,vegetable,meats]
# print(groceries)

# print(groceries[0][2])
for collection in groceries:
    print(collection)
    for foods in collection:
        print(foods,end=" ")
    print()

#dictionary= a collection of {key:value} pairs
#            ordered and changeable. No duplicates

capitals={"USA":"Washington D.C.",
          "Nepal":"Kathmandu"}
#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("China"))
#It returns None

capitals.update({"Germany":"Berlin"})
capitals.update({"Germany":"Your mum"})

capitals.pop("USA")
capitals.popitem()#Removes the latest one
# capitals.clear()

#keys= capitals.keys()
#USA, Nepal, etc

#values=capitals.values()

items=capitals.items()
for key,value in items:
    print(f"{key}:{value}")
print("\n\n\n")

#Concession stand program
menu={"popcorn":270,
        "burger":300,
        "coke":100,
        "nachos":350,
        "pizza":300,
        "water":75
        }
cart=[]
total=0

print("--------------- Menu ---------------")
for key,value in menu.items():
    print(f"{key:10}:Rs.{value:.2f}")
print("------------------------------------")

while True:
    food=input("Select an item(q to quit)").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
         cart.append(food)
print("----------YOUR ORDER-------------")
for food in cart:
    total+= menu.get(food)
    #.get(key) is a dictionary method that
    # returns the value associated with the key (if it exists).
    print(food, end=" ")
print()
print(f"Your total is Rs.{total:.2f}")
print("---------------------------------")
   





 


