class user:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        # print(f"user: {self.name}")
        print("$" + str(self.amount))
        return self


Alberto = user("Alberto")
Dylan = user("Dylan")
Daniel = user("Daniel")

Alberto.make_deposit(100).make_deposit(50).make_deposit(50).make_withdrawal(25).display_user_balance()

Dylan.make_deposit(900).make_deposit(700).display_user_balance()

Daniel.make_deposit(10000).make_withdrawal(1000).make_withdrawal(5000).make_withdrawal(3000).display_user_balance()