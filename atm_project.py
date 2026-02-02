class ATM:
    def __init__(self):
        self.pin = self.load_pin()
        self.balance = self.load_balance()

    # ---------- LOAD / SAVE ----------
    def load_pin(self):
        try:
            with open("pin.txt", "r") as f:
                return f.read().strip()
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

    # ---------- COMMON DISPLAY + SAVE ----------
    def log(self, message):
        print(message)
        with open("history.txt", "a") as f:
            f.write(message + "\n")

    def screen_header(self, title):
        print(f"\n===== {title} =====")

    def screen_footer(self):
        print("==============================")

    # ---------- SCREENS ----------
    def check_balance(self):
        self.screen_header("BALANCE SCREEN")
        msg = f"Available Balance : {self.balance}"
        self.log(msg)
        self.screen_footer()

    def deposit(self, amount):
        self.screen_header("DEPOSIT SCREEN")
        if amount > 0:
            self.balance += amount
            self.save_balance()
            msg = f"Deposit Successful | Amount : {amount} | Balance : {self.balance}"
            self.log(msg)
        else:
            self.log("Deposit Failed | Invalid Amount")
        self.screen_footer()

    def withdraw(self, amount):
        self.screen_header("WITHDRAW SCREEN")
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.save_balance()
            msg = f"Withdraw Successful | Amount : {amount} | Balance : {self.balance}"
            self.log(msg)
        else:
            self.log("Withdraw Failed | Insufficient Balance")
        self.screen_footer()

    def show_history(self):
        self.screen_header("TRANSACTION HISTORY SCREEN")
        try:
            with open("history.txt", "r") as f:
                data = f.read()
                if data.strip() == "":
                    print("No transactions available")
                else:
                    print(data)
        except:
            print("No history file found")
        self.screen_footer()

    def download_statement(self):
        self.screen_header("STATEMENT DOWNLOAD SCREEN")
        with open("statement.txt", "w") as f:
            f.write("ATM STATEMENT\n")
            f.write("-----------------------------\n")
            f.write(f"Current Balance : {self.balance}\n\n")
            f.write("Transaction History:\n")
            try:
                with open("history.txt", "r") as h:
                    f.write(h.read())
            except:
                f.write("No transactions")
        self.log("Statement Downloaded Successfully")
        self.log("Saved as : statement.txt")
        self.screen_footer()

    def exit_screen(self):
        self.screen_header("EXIT SCREEN")
        self.log("Thank you for using ATM")
        self.log("Please collect your card")
        self.screen_footer()


# ---------------- MAIN PROGRAM ----------------

atm = ATM()

# ---------- PIN SCREEN ----------
attempts = 0
while attempts < 3:
    atm.screen_header("PIN VERIFICATION SCREEN")
    entered_pin = input("Enter your PIN : ")
    if entered_pin == atm.pin:
        print("PIN Verified Successfully")
        atm.screen_footer()
        break
    else:
        attempts += 1
        print("Wrong PIN")
        atm.screen_footer()

if attempts == 3:
    atm.screen_header("ATM BLOCKED SCREEN")
    print("Too many wrong attempts")
    print("ATM is temporarily blocked")
    atm.screen_footer()

else:
    while True:
        print("\n========= ATM MAIN MENU =========")
        print("1. Balance Enquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Download Statement")
        print("6. Exit")
        print("================================")

        choice = input("Select option : ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amt = int(input("Enter deposit amount : "))
            atm.deposit(amt)

        elif choice == "3":
            amt = int(input("Enter withdraw amount : "))
            atm.withdraw(amt)

        elif choice == "4":
            atm.show_history()

        elif choice == "5":
            atm.download_statement()

        elif choice == "6":
            atm.exit_screen()
            break

        else:
            atm.screen_header("INVALID OPTION SCREEN")
            print("Please select a valid option")
            atm.screen_footer()
