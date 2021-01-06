

class Account():
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
 

    def deposit(self,ammount):
        print (f"Account : {self.owner} depositing {ammount}")
        self.balance = self.balance + ammount
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}" + "\n" +  f"Account Balance: {self.balance}"

    def withdraw(self,ammount):
        print (f"Account : {self.owner} withdrawing {ammount}")
        if ammount > self.balance :
            print ("Funds unavaliable , you are trying to withdraw to much money you greedy git")
        else:
            self.balance = self.balance - ammount
        
        return self.balance
    
        



acc1=Account("Simon", 100)


print (acc1)

print (acc1.balance)
acc1.deposit(100)
print (acc1)
acc1.withdraw(100)
print (acc1)
print (acc1.balance)
acc1.withdraw(100)
print (acc1.balance)
acc1.withdraw(100)