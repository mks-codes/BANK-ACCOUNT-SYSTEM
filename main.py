from abc import ABC, abstractmethod

class BankSecurity(ABC):

    @abstractmethod
    def security(self):
        pass

customers = []

class BankAccount(BankSecurity):
    def __init__(self):
        pass
    
    def Deposit(self,pin,money):
        for user in customers:
            if user['pin'] == pin:
                 user['money'] += money
        return user['money']
    def __str__(self):
        return f"{self.user}"
   

    def Withdraw(self,pin,money):
        for user in customers:
            if user['pin'] == pin:
                 user['money'] -= money
        return user['money']

    def CheckBalance(self,pin):
         for user in customers:
            if user['pin'] == pin:
                return user['money']
            
    def InterestCalculation(self,pin):
        for user in customers:
            if user['pin'] == pin:
                 interest = user['money'] * 5 * 1 /100
        return interest

    def security(self):
        pass 

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__(self)
        pass

class CurrentAccount(BankAccount):
    def __init__(self):
        super().__init__(self)
        pass

class AccountHolders:
    def __init__(self,name,account_no,money,pin):
        self.name = name
        self.account_no = account_no
        self.money = money
        self.pin = pin

    def to_dict(self):
        customers.append({"name":self.name, "account":self.account_no, "money":self.money, "pin":self.pin})

holder = AccountHolders('mks',8080981549,500,"00")
holder.to_dict()

user = BankAccount()
print(user.Deposit("00",100))
print(user.Withdraw("00",150))
print(user.CheckBalance("00"))
print(user.InterestCalculation("00"))