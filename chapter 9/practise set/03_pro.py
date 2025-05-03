class BankAccount:
    def __init__(self,owner,balance=0): #will initalize automaticlly  
        self.owner = owner
        self.balance = balance


    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited ₹{amount}. new balance : ₹{self.balance} ")

        else:
            print("Deposit must be postive")


    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} has withdrew ₹{amount}. remaining balance ₹{self.balance}")
        else:
            print("Insufficient balance.")


    
    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"₹{amount} transferred to {other_account.owner}")
        else:
            print("Transfer failed: Not enough balance.")


    def check_balance(self):
        print(f"{self.owner}'s current balance ₹{self.balance}")


name1 = input("Enter the name for first account : ")
balance1 = float(input(f"Enter the start balance for {name1} : "))
account1 = BankAccount(name1,balance1)

name2 = input("Enter the name for second account : ")
balance2 = float(input(f"Enter the start balance for {name2} :"))
account2 = BankAccount(name2,balance2)


while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        who = input("Deposit to which account? (1 or 2): ")
        amount = float(input("Enter amount to deposit: "))
        if who == "1":
            account1.deposit(amount)
        else:
            account2.deposit(amount)

    elif choice == "2":
        who = input("Withdraw from which account? (1 or 2): ")
        amount = float(input("Enter amount to withdraw: "))
        if who == "1":
            account1.withdraw(amount)
        else:
            account2.withdraw(amount)

    elif choice == "3":
        direction = input("Transfer from 1 to 2 or 2 to 1? (1/2): ")
        amount = float(input("Enter amount to transfer: "))
        if direction == "1":
            account1.transfer(account2, amount)
        else:
            account2.transfer(account1, amount)

    elif choice == "4":
        print("\nBalance Info:")
        account1.check_balance()
        account2.check_balance()

    elif choice == "5":
        print("Thank you for using the bank system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")


