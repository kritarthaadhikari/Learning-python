import random
#random module
#print("\u25CF \u250C \u2500 \u2510 \u2514 \u2518") unicode characters 
#  for the symbols of the dice
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice=[]
total=0
num_of_dice=int(input("How many dice you want?"))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for x in dice:
    total+=x

# for vertical
# for y in range(num_of_dice):
#     for line in dice_art.get(dice[y]):
#         print(line)

#for horizontal
for line in range(5):
    for x in dice:
        print(dice_art.get(x)[line],end=" ")
    print()

 
print(f"Total:{total}")




