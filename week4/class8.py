

#################################################################

class bank_acct:
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        self.balance -= amount
        return self

    def display_acct_bal(self):
        print("New balance is", self.balance)
        return self
##########################################################################

class user:
    def __init__(self, name, id) :
        self.name=name
        self.id=id
        self.acct_bal=bank_acct(0, 0.05) # (Balance, intrest rate)

    def deposit(self, amount):
        self.acct_bal.make_deposit(amount)
        print("Adding $",amount, "to",self.name+"'s account", self.id)
        return self

    def withdraw(self, amount):
        self.acct_bal.make_withdraw(amount)
        print("Withdrawing $",amount, "from",self.name+"'s account", self.id)
        return self

    def transfer_amt(self, other_user, amount):
        other_user.deposit(amount)
        self.withdraw(amount)

jack = user("Jack","id005")
jack.deposit(1000).acct_bal.display_acct_bal()
jack.withdraw(500).acct_bal.display_acct_bal()
 


# acct1=bank_acct(10000,0.025,"Acct1")
# acct2=bank_acct(20000,0.04,"Acct2")

# acct1.display_acct_bal()
# acct1.make_deposit(500)
# acct1.display_acct_bal()


# customer1=user("Prasant","12345",90)
# print(customer1) ## This prints address of customer1
# print("customer1 Name:",customer1.name)
# print("customer1 initial Acct Bal:", customer1.acct_bal)
# customer1.deposit(100)
# print("customer1 Acct Bal after deposit:",customer1.acct_bal)
# print("*********************************\n")
# customer2=user("Ala","X12345",1000)
# print("customer2:",customer2.name+"'s", "Acct Bal:",customer2.acct_bal)
# customer3=user("Red","B12345",1000)
# print("customer3:",customer3.name+"'s", "Acct Bal:",customer3.acct_bal)
# customer2.transfer_amt(customer3,500)
# print("****Tansfer 500 from customer2 to customer3*****")
# print("cutomer2:",customer2.name+"'s", "Acct Bal after tansfer:",customer2.acct_bal)
# print("cutomer3:",customer3.name+"'s", "Acct Bal after tansfer:",customer3.acct_bal)