#Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def withdrawal(balance):
    amount=float(input("Enter the amount you want to withdraw "))
    if amount>0:
        if amount>balance:
            print("Insufficient funds")
        else:
            return amount
    else:
        print("Not a valid amount")

def deposit():
    amount=float(input("Enter the amount to be deposited "))
    if amount>=0:
        return amount
    else:
        print("Not a valid amount")

def main():
    balance=0
    isRunning=True

    while isRunning:
        print("------------Welcome To Banking System--------------")
        print("Pick the service you want to exercise")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice=input("Enter your choice(1-4) ")

        if choice=='1':
            show_balance(balance)

        elif choice=='2':
            balance+=deposit()
            print(f"Your balance is ${balance:.2f}")

        elif choice=='3':
            balance-=withdrawal(balance)
            print(f"Your balance is ${balance:.2f}")

        elif choice=='4':
            isRunning=False

        else:
            print("Not a valid choice!")

if __name__=='__main__':

    main()


    