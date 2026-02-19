from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,account_number,account_holder,balance,status="ACTIVE"):
        self._account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance
        self._status = status

    # get account number
    def get_account_number(self):
        return self._account_number
    
    # get account holder
    def get_account_holder(self):
        return self._account_holder
    
    # get balance 
    def get_balance(self):
        return self.__balance
    
    # Status
    def is_active(self):
        return self._status == "ACTIVE"
    
    # Freeze account
    def freeze_account(self):
        self._status = "FROZEN"

    # Activate frozen account
    def activate_account(self):
        self._status = "ACTIVE"

    # deposit amount
    def deposit(self,amount):
        if not self.is_active():
            raise Exception("Account is frozen.")
        if amount <= 0:
            raise ValueError("Deposit amount mustbe positive.")
        self.__balance += amount
        return self.__balance
    
    # update balance
    def _update_balance(self, new_balance):
        self.__balance = new_balance
    
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def calculate_interest(self):
        pass
    
