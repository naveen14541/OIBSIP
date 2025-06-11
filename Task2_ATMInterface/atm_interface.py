class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Deposited Rs.{amount}. Current Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print(f"Withdrew Rs.{amount}. Current Balance: Rs.{self.balance}")

    def transfer(self, amount, account):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Transferred: {amount} to Account {account}")
            print(f"Transferred Rs.{amount} to Account {account}. Current Balance: Rs.{self.balance}")

    def transaction_history(self):
        print("\n--- Transaction History ---")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print(t)

    def check_balance(self):
        print(f"\n Current Balance: Rs.{self.balance}")
        
def main():
    print("Welcome to the ATM Interface!")
    print("This project is developed by Naveen Thummala.\n")

    user_id = "naveen123"
    user_pin = "1234"

    entered_id = input("Enter User ID: ")
    entered_pin = input("Enter PIN: ")

    if entered_id == user_id and entered_pin == user_pin:
        print("\nLogin Successful!\n")
        atm = ATM(balance=1000) 

        while True:
            print("\n--- ATM Menu ---")
            print("1. Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Check Balance")
            print("6. Quit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                atm.transaction_history()
            elif choice == '2':
                amount = int(input("Enter amount to withdraw: Rs."))
                atm.withdraw(amount)
            elif choice == '3':
                amount = int(input("Enter amount to deposit: Rs."))
                atm.deposit(amount)
            elif choice == '4':
                amount = int(input("Enter amount to transfer: Rs."))
                account = input("Enter account number to transfer to: ")
                atm.transfer(amount, account)
            elif choice == '5':
                atm.check_balance()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid User ID or PIN!")

if __name__ == "__main__":
    main()
