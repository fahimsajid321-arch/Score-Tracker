class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
    def display_balance(self):
        print(f"Your balance is {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance = self.balance + (self.balance*self.interest_rate)
        print(f"Amount after adding interest is {self.balance}")
        
class CheckAccount(BankAccount):
    def __init__(self, account_holder, balance, Overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = Overdraft_limit
    def Withdrawl_Amount(self, withdrwal_amount):
        if (self.balance + self.overdraft_limit) >= withdrwal_amount:
            print(f"{withdrwal_amount} has been WithDrawl")
            self.balance = self.balance - withdrwal_amount
            print(f"{self.balance}") 
        else:
            print("Error: Limit Exceeded")


