class ATM:
    def __init__(self):
        self.pin = self.load_pin()
        self.balance = self.load_balance()

    def load_pin(self):
        try:
            with open("pin.txt", "r") as f:
                return f.read()
        except:
            with open("pin.txt", "w") as f:
                f.write("1111")   
            return "1111"

    def load_balance(self):
        try:
            with open("balance.txt", "r") as f:
                return int(f.read())
        except:
            with open("balance.txt", "w") as f:
                f.write("0")
            return 0

    def save_balance(self):
        with open("balance.txt", "w") as f:
            f.write(str(self.balance))

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save_balance()
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.save_balance()
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


atm = ATM()

# 🔐 PIN Verification
entered_pin = input("Enter your PIN: ")

if entered_pin != atm.pin:
    print("Incorrect PIN. Access Denied.")
else:
    print("PIN verified successfully")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amt = int(input("Enter amount to deposit: "))
            atm.deposit(amt)
        elif choice == "3":
            amt = int(input("Enter amount to withdraw: "))
            atm.withdraw(amt)
        elif choice == "4":
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")
