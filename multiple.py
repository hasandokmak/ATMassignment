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
    print("Welcome to the ATM")
    print("1. CHECK BALANCE")
    print("2. DEPOSIT MONEY")
    print("3. WITHRAW MONEY")
    print("4. EXIT")

    num = input("Choose Ur Option")

    if num == "1":
        print(f"ur balance is {balance} $")
    elif num == "2":
        amount = float(input("Enter Deposit Amount"))
        balance += amount
        print(f"Deposited {amount}$.\nNew Balance: {balance}$.")
    elif num == "3":
        withdr =  float(input("Enter Withdrawal Amount"))
        if amount > balance:
            print("Error")
        else: 
            balance = balance - amount
    elif num == "4":
        print("Exiting")
        break
    else:
        print("No such option")
