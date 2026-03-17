balance = float(input("Enter initial balance: "))
while True:
    print("\n----- Banking Menu -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current Balance = Rs.", balance)
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount deposited successfully")
    elif choice == 3:
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful. Please collect your cash.")
        else:
            print("Error: Insufficient balance")
    elif choice == 4:
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
