def withdraw():
    amount = int(input(" Enter the amount you want to withdraw"))
    if amount<0:
        print("Entered value should be positive")
    elif(amount > balance):
        print("Insufficient funds")
        return 0
    else:
        print("Withdrawl Succesful")
        return amount   
def check_balance():
    print(f" Account balance is {balance}")

def deposit():
    amount = int(input("Enter amount you want to deposit"))
    if(amount > 0):
        return amount
    else:
        print("Entered value should be positive")
        return 0
def exit():
    print("Exiting..")

print(" Banking operations")

balance = 0


isRunning = True

while isRunning:
    print(" Select an option from below")
    print("1. Withdraw 2. Balance enquiry 3. Deposit 4.Exit")

    choice = input(" Enter your choice")


    if choice == '1':
        balance -= withdraw()

    elif choice == '2':
        check_balance()

    elif choice == '3':
         balance += deposit()

    elif choice == '4':
        exit()
        isRunning = False

    else:
        print(" Not a valid choice")

