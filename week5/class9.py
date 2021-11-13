

#################################################################


##########################################################################

class user:
    def __init__(self, name, id, balance) :
        self.name=name
        self.id=id
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def transfer_amt(self, other_user, amount):
        other_user.deposit(amount)
        self.withdraw(amount)

class bank_acct(user):
    def __init__(self, name, id, balance, int_rate):
        super().__init__(name,id,balance)
        self.int_rate = int_rate

    def make_deposit(self, amount):
        super().deposit(amount)

    def diaply_acct_bal(self):
        print(self.name, "Balance", self.balance)
        return self

jack = bank_acct("Jack", "id005", 0, 0.25)
jack.make_deposit(7000)
jack.diaply_acct_bal()        