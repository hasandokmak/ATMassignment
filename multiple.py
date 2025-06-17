balance = 1000
passw = "hsn33"
transaction = 0
failed = 0

enterpass = input("Password? ")
if enterpass != passw:
    print("WRONG")
    exit()

bool = True
while bool:
    print("\nWelcome to the ATM")
    print("1. CHECK BALANCE ")
    print("2. DEPOSIT MONEY ")
    print("3. WITHRAW MONEY ")
    print("4. EXIT ")

    num = input("\nChoose Ur Option: ")

    if num == "1":
        print(f"ur balance is {balance} $")
        transaction+=1
    elif num == "2":
        
        amount = float(input("\nEnter Deposit Amount: "))
        if amount < 0:
            print("Invalid")
        else:
            balance += amount
            print(f"\nDeposited {amount}$.\nNew Balance: {balance}$.\n")
            transaction+=1
    elif num == "3":
        withdr =  float(input("\nEnter Withdrawal Amount: "))
        if withdr <= 0:
            print("Invalid")
        elif withdr > balance:
            print("Error")
            failed += 1
            if failed > 3:
                print("Warning, more than 3 withdrawal attempts have failed")
        else: 
            balance = balance - withdr
            print(f"\nWithdrew {withdr}$.\nNew Balance: {balance}$.\n")
            transaction+=1
    elif num == "4":
        print(f"nb of transactions done: {transaction}\n")
        print("Exiting")
        break
    else:
        print("No of such option")
