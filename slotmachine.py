#Python Slot Machine

import random

def spin_row():
    symbols=['🍒','🍋','🔔','⭐','🍉']
    # results=[]

    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    #or
    return [random.choice(symbols) for _ in range(3)]# _ is a placeholder

def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*2
        
        elif row[0]=='🍉':
            return bet*3
        
        elif row[0]=='⭐':
            return bet*4
        
        elif row[0]=='🍋':
            return bet*6
        
        elif row[0]=='🔔':
            return bet*8
    else: 
        return 0   

def main():
    balance=100
    print("-----------------------")
    print("Welcome to Python Slots")
    print("-----------------------")
    print("Symbols: 🍒 🍉 🍋 ⭐ 🔔")
    print("-----------------------")

    while balance>0:
        print(f"Your current balance is ${balance}")
        bet=input("Place your bet")

        if not bet.isdigit():
            print("Enter a valid amount")
            continue

        bet=int(bet)

        if bet > balance:
            print("Insufficient balance")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet
        row=spin_row()
        print("Spinning........")
        print_row(row)

        payout=get_payout(row,bet)
        if payout>0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you lost this round")
        balance+=int(payout)
        print(f"Your balance is ${balance}")

        play_again=input("Do you want to play again?(y/n)")
        if play_again.upper()!='Y':
            break

if __name__=='__main__':
    main()