class user:
    def __init__(self,name,id,acct_bal) :
        self.name=name
        self.id=id
        self.acct_bal=acct_bal

    def deposit(self,amount):
        self.acct_bal += amount
        return self

    def withdraw(self,amount):
        self.acct_bal -= amount
        return self

    def transfer_amt(self,other_user,amount):
        other_user.deposit(amount)
        self.withdraw(amount)            

customer1=user("Prasant","12345",90)
print(customer1) ## This prints address of customer1
print("customer1 Name:",customer1.name)
print("customer1 initial Acct Bal:", customer1.acct_bal)
customer1.deposit(100)
print("customer1 Acct Bal after deposit:",customer1.acct_bal)
print("*********************************\n")
customer2=user("Ala","X12345",1000)
print("customer2:",customer2.name+"'s", "Acct Bal:",customer2.acct_bal)
customer3=user("Red","B12345",1000)
print("customer3:",customer3.name+"'s", "Acct Bal:",customer3.acct_bal)
customer2.transfer_amt(customer3,500)
print("****Tansfer 500 from customer2 to customer3*****")
print("cutomer2:",customer2.name+"'s", "Acct Bal after tansfer:",customer2.acct_bal)
print("cutomer3:",customer3.name+"'s", "Acct Bal after tansfer:",customer3.acct_bal)
