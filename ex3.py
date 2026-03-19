foods=[]
prices=[]
n=0
total=0
while True:
    food=input("Enter a food to buy(Enter q to quit)")
    if food.lower()=="q":
        break
    else:
        n+=1
        price=float(input("Enter the price"))
        foods.append(food)
        prices.append(price)
print("-----Your Cart------")

for x in range(n):
    print(f"{foods[x]:<20}",end=" ")
    print(prices[x])
    print()
    total+=prices[x]
print(f"{total:20}")


#Numpad
num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()




       
     
