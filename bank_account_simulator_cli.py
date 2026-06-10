class Account:
    def __init__(self, owner: str, account_number: str, balance: int):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.account_type = "Checking"
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("You can only deposit amounts greater than zero")
        else:
            self.__balance +=amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError ("Your balance is lower than your amount of withdraw")
        else:
            self.__balance -=amount
    
    def transfer(self, amount, target_account):
        self.withdraw(amount)
        target_account.deposit(amount)
    
    @property
    def balance(self):
        return self.__balance
    
    def get_summary(self):
        return f"Account: {self.owner} | Account_balance : ${self.balance}"
    
    def __str__(self):
        return f"Account owner: {self.owner.title()} | Account_number: {self.account_number} | Account_balance: ${self.balance}| Account Type: {self.account_type}"
        
class SavingsAccount(Account):
    def __init__(self, owner: str, account_number: str, balance: int, interest_rate: float):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
        self.account_type = "Savings"
    
    def calculate_simple_interest(self, years):
        return self.balance * self.interest_rate * years
    
    def calculate_compound_interest(self, years, n=12):
        P = self.balance
        r = self.interest_rate
        A = P * (1 + r/n) ** (n * years)
        return A - P 
    
    def interest_projection(self):
        periods = [
                ("1 month",   1/12),
                ("6 months",  6/12),
                ("12 months", 12/12),
                ]

        print(f"=== Interest Projection (Rate: {self.interest_rate * 100}%) ===")
        print(f"{'Period':<15} {'Simple':>10} {'Compound':>10}")
        print("-" * 37)

        for label, years in periods:
            simple   = self.calculate_simple_interest(years)
            compound = self.calculate_compound_interest(years)
            print(f"{label:<15} ${simple:>9.2f} ${compound:>9.2f}") 
    
    def get_summary(self):
        summary = super().get_summary()
        return f"{summary} | Interst_rate: {self.interest_rate}"

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.__accounts = {}
    
    def create_account(self, owner_name, account_type, opening_deposit):
        
       account_number = f"ACC-{len(self.__accounts) + 1:03d}"
    
       if account_type == "Savings":
           account = SavingsAccount(owner_name, account_number, opening_deposit, 0.05)
       else:
           account = Account(owner_name, account_number, opening_deposit)
    
       self.__accounts[account_number] = account
       
       print(f"Account created successfully. Your account number is {account_number}")
    
    def get_account(self, account_number):
        return self.__accounts.get(account_number, None)
    
    def list_accounts(self):
        for account in self.__accounts.values():
            print(account)

    
    def total_assets_report(self):
        checking_total = 0
        savings_total = 0
        for account in self.__accounts.values():
            if account.account_type == "Checking":
                checking_total += account.balance
            else:
                savings_total += account.balance
        print("=======================TOTAL REPORT=======================")
        print(f"Account_type: Regular account | Total: ${checking_total}")
        print(f"Account_type: Savings Account | Total: ${savings_total}")
        print(f"Total of all accounts: ${checking_total+savings_total}")
    
def menu():
        print("\n========== MENU ==========")
        print("1. Open New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View account details")
        print("6. View all accounts")
        print("7. Interest projection")
        print("8. Bank report")
        print("9. Exit")
        print("==========================")

def main():
    bank = Bank("First Bank of Elizabeth")
    
    while True:
        menu()
        option = input("Choose an option: ").strip()
        
        if option == "1":
            owner = input("Enter your name: ").strip()
            account_type = input("Account type (Checking/Savings): ").strip().capitalize()
            opening_deposit = float(input("Opening deposit amount: $"))
            bank.create_account(owner, account_type, opening_deposit)
        
        elif option == "2":
            account_number = input("Enter account number: ").strip().upper()
            account = bank.get_account(account_number)
            if account is None:
                print("Account not found.")
            else:
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)
                print(f"Deposited successfully. New balance: ${account.balance:.2f}")
        
        elif option == "3":
            account_number = input("Enter account number: ").strip().upper()
            account = bank.get_account(account_number)
            if account is None:
                print("Account not found.")
            else:
                amount = float(input("Enter withdraw amount: $"))
                account.withdraw(amount)
                print(f"Withdraw was successful. New balance: ${account.balance:.2f}")
        
        elif option == "4":                                         
            from_number = input("Enter YOUR account number: ").strip().upper()
            from_account = bank.get_account(from_number)
            if from_account is None:
                print("Source account not found.")
            else:
                to_number = input("Enter DESTINATION account number: ").strip().upper()
                to_account = bank.get_account(to_number)
                if to_account is None:
                    print("Destination account not found.")
                else:
                    amount = float(input("Enter transfer amount: $"))
                    try:
                        from_account.transfer(amount, to_account)
                        print(f"Transfer successful.")
                        print(f"  Your new balance:          ${from_account.balance:.2f}")
                        print(f"  Destination new balance:   ${to_account.balance:.2f}")
                    except ValueError as e:
                        print(f"Error: {e}")
        
        elif option == "5":                                         
            account_number = input("Enter account number: ").strip().upper()
            account = bank.get_account(account_number)
            if account is None:
                print("Account not found.")
            else:
                print(account.get_summary())
        
        elif option == "6":
             bank.list_accounts()
            
        
        elif option == "7":                                         
            account_number = input("Enter account number: ").strip().upper()
            account = bank.get_account(account_number)
            if account is None:
                print("Account not found.")
            elif not isinstance(account, SavingsAccount):
                print("Interest projection is only available for Savings accounts.")
            else:
                account.interest_projection()
        
        elif option == "8":
             bank.total_assets_report()
             
        
        elif option == "9":
            print("Goodbye.")
            break
if __name__ == "__main__":
    main()

