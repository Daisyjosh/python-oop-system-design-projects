from models.account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000

    def withdraw(self,amount):
        if not self.is_active():
            raise Exception("Account is Frozen")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        current_balance = self.get_balance()
        new_balance = current_balance - amount
        if new_balance < self.OVERDRAFT_LIMIT:
            raise ValueError("Overdraft limit exceeded.")

        self._update_balance(new_balance)
        return new_balance
    

    def calculate_interest(self):
        return 0