import random
# number=random.randint(1,6)
# print(number)
#number= random.random() 
#gives a random floating point number

#Rock,Paper,Scissor idea
options= ("scissor","paper","rock")
option=random.choice(options)
print(option)

#Deck of Cards Shuffling
cards= ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)

#Number guessing game
guesses=0
low=0
high=100
number=random.randint(low,high)

while True:
    guess=int(input(f"Enter a number between {low}- {high}"))
    guesses+=1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!")
        print(f"It took you {guesses} guesses")
        break


#Rock Paper Scissor Game
print("-----------Welcome to Rock, Paper, Scissors-----------")
options=["rock","paper","scissors"]
running= True

while running:
    player= None
    computer=random.choice(options)

    while player not in options:
        player=input("Enter a choice:(Rock,Paper,Scissors)").lower()

    print(f"Player:{player}\nComputer:{computer}")
    print()

    if player=="rock" and computer=="scissors":
        print("You win!")
        print()

    elif player=="paper" and computer=="rock":
        print("You win!")
        print()

    elif player=="scissors" and computer=="paper":
        print("You win!")
        print()

    elif player==computer:
        print("It's a tie")
        print()

    else:
        print("You lose!")
        print()

    play_again=input("Do you want to play again?(y or n)")
    while play_again!="y" and play_again!="n":
         play_again=input("Do you want to play again?(y or n)")
         print()
         
    if play_again=="y":
        running=True
    elif play_again=="n":
        running=False
print("------------------Thanks for playing!-----------------")