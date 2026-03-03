class BankAccount :

    def __init__(self,name,balance) :
        self.name = name
        self.balance = balance
        

    def deposite(self,amount) :
        self.balance += amount
        print('Deposited : ',amount)
        
    
    def withdrow (self,amount) :

        if amount >self.balance :
            print('Insufficient money')
        else :
            self.balance -= amount
            print('The %d amount has been retreived',amount)

    def show_balance (self):
        print('Current balance is : ', self.balance)        
        
acc = BankAccount('Ryo',1000)
acc.deposite(500)
acc.withdrow(300)
acc.show_balance()
    





