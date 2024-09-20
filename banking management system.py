class Account:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance -= amount
            print(f"Deposited ${amount} into account {self.account_number}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance += amount
                print(f"Withdrew ${amount} from account {self.account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def transfer(self, amount, target_account):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                target_account.deposit(amount)
                print(f"Transferred ${amount} from account {self.account_number} to account {target_account.account_number}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")
    
    def get_balance(self):
        return self.balance
    
    def _str_(self):
        return f"Account Number: {self.account_number}, Owner: {self.owner}, Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        if account.account_number not in self.accounts:
            self.accounts[account.account_number] = account
            print(f"Account {account.account_number} created.")
        else:
            print("Account number already exists.")
    
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
    
    def display_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            print("\nBank Accounts:")
            for account in self.accounts.values():
                print(account)
    
    def transfer_funds(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account and to_account:
            from_account.transfer(amount, to_account)
        else:
            print("Invalid account numbers.")

def main():
    bank = Bank()
    
    while True:
        print("\nSimple Banking System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Balance")
        print("6. View All Accounts")
        print("7. Exit")
        
        choice = input("Select an option (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            account_number = input("Enter account number: ")
            owner = input("Enter account owner name: ")
            initial_balance = float(input("Enter initial balance (default is 0): ") or 0)
            account = Account(account_number, owner, initial_balance)
            bank.add_account(account)
        elif choice == '2':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            from_account_number = input("Enter source account number: ")
            to_account_number = input("Enter target account number: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer_funds(from_account_number, to_account_number, amount)
        elif choice == '5':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Balance of account {account_number}: ${account.get_balance():.2f}")
            else:
                print("Account not found.")
        elif choice == '6':
            bank.display_accounts()
        elif choice == '7':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        
        # Optional: Add a separator for better readability
        print("\n" + "-"*30)

if __name__ == "__main__":
    main()
