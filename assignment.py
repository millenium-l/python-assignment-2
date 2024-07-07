# input
cash = 1000
option = 0 # i initialize

# we loop 
while option <=4:  
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    option = int(input("Enter any provided option: "))

    # check amount of money
    if option == 1:
        print(f"Your current balance is: {cash}")

    # add money to my account
    elif option == 2:
        deposit_money = float(input("Enter amount to deposit: "))
        cash += deposit_money
        print(f"You have deposited {deposit_money}. Your new balance is: {cash}")

    # take money from my account
    elif option == 3:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= cash:
            cash -= withdraw_amount
            print(f"You have withdrawn {withdraw_amount}. Your new balance is: {cash}")
        else:
            print("Insufficient funds.")

    # exit the program
    elif option == 4:
        print("Exit the program.")
        break
    else:
        print("Invalid option. Please choose a valid option.")
