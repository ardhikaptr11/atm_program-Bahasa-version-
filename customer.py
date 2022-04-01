from numpy import append
from atm_card import ATMCard

class Customer:

    def __init__(self, id, custPin = 228181, custBalance = 100000): 
        self.id = id 
        self.balance = custBalance
        self.custPin = custPin

    def checkId(self): 
        return self.id

    def checkBalance(self):
        return self.balance

    def checkPin(self):
        return self.custPin

    def withdrawBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal


    



