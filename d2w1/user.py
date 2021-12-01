class user:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        # print(f"user: {self.name}")
        print("$" + str(self.amount))


Alberto = user("Alberto")
Dylan = user("Dylan")
Daniel = user("Daniel")

Alberto.make_deposit(100)
Alberto.make_deposit(50)
Alberto.make_deposit(50)
Alberto.make_withdrawal(25)
Alberto.display_user_balance()

Alberto.display_user_balance()

Dylan.make_deposit(100)
Dylan.make_deposit(700)
Dylan.make_withdrawl(500)
Dylan.make_withdrawl(300)
Dylan.display_user_balance()

Daniel.make_deposit(10000)
Daniel.make_withdrawl(1000)
Daniel.make_withdrawl(5000)
Daniel.make_withdrawl(3000)
Daniel.display_user_balance()