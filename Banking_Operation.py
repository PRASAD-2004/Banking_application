from abc import ABC,abstractmethod

class checkabstract(ABC):

    @abstractmethod
    def checkbalance(self):
        pass
    
    
class Bank(checkabstract):
    def __init__(self,accname,bal) -> None:
        self.accname=accname
        self.bal=bal

        print(f"\n Account '{self.accname}' created. \n Balance is {self.bal:.2f}")

    def deposit(self,depositamount):
        self.bal+=depositamount
        print("deposit successfull")
        self.checkbalance()
    
    def checkbalance(self):
        print(self.accname,"balance is ",self.bal)

    
    def withdraw(self,withdrawamount):
        if self.bal<withdrawamount:
            print("insufficient balance in",self.accname,"account")
        else:
            self.bal-=withdrawamount
            print("withdraw successful")
            self.checkbalance()

    def transfer(self,amount,acccname):
        print("transfer beginning...")
        if self.bal<amount:
            print("insufficient balance in",self.accname,"account")
        else:
            self.bal-=amount
            acccname.deposit(amount)
            print("amount transfered successfully")
            self.checkbalance()
            acccname.checkbalance()
            print("transfer completed")



