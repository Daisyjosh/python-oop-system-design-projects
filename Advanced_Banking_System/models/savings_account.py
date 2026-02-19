from models.account import Account

class SavingsAccount(Account):
    MINIMUM_BALANCE = 1000
    INTEREST_RATE = 0.04 # 4% 
    OVERDRAFT_LIMIT = 1000

    def withdraw(self,amount):
        if not self.is_active():
            raise Exception("Account is Frozen")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if self.get_balance() - amount < self.MINIMUM_BALANCE:
            raise ValueError("Cannot withdraw. Minimum balance required violated.")
        
        current_balance = self.get_balance()
        new_balance = current_balance - amount
        if new_balance < -self.OVERDRAFT_LIMIT:
            raise Exception("Overdraft limit exceeded")

        self._update_balance(new_balance)
    
    def calculate_interest(self):
        interest = self.get_balance()*self.INTEREST_RATE
        new_balance = self._Account__balance + interest
        self._Account__balance = new_balance
        return interest
    