#create a python class calle bank account which represents a bank account having attributes acc no, name, balance, 
#create a constructor with parameteres acc no, name, balance      create a deposit method which manages 
#deposit action
#create a withdrawl which manages withdrawl actions
#create a bank fees method to apply bank fees with a precentage of 5% of the balance account
#create a display method to display account detail
class bankAccount:
    def __init__(self, accNo, name, balance):
        self.accNo = accNo
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance+= amount
    def withdrawal(self,amount):
        self.balance-=amount
    def bankFees(self):
        return (self.balance*5/100) 
    def display(self):
        print(self.accNo,self.name,self.balance)

newAcc = bankAccount(1,"Ayush",10000)
newAcc.deposit(100)
newAcc.withdrawal(1000)
print(newAcc.bankFees())
newAcc.display()


        