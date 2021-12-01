class BankAccount:

    def __init__(self, int_rate, balance): 
        self.deposit = deposit
        self.withdraw = withdraw
        self.int_rate = 2
        self.balance = 0
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.amount += amount
        return self
        # your code here

    def withdraw(self, amount):
        self.amount -= amount
            if amount <= 0
        print("Insufficient funds: Charging a $5 fee")
        return self
        # your code here

    def display_account_info(self):
        print("$" + str(self.amount))
        return self
        # your code here
    def yield_interest(self):
        self.int_rate * balance
        if balance <= 0
        continue
        # your code here

acc1 = BankAccount("acc1")
acc2 = BankAccount("acc2")

acc1.deposit(100).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()
acc2.deposit(175).deposit(225).withdraw(50).withdraw(100).withdraw(10).withdraw(10).yield_interest().display_account_info()