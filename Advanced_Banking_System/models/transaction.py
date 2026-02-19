from datetime import datetime

class Transaction:
    def __init__(self,account_number,transaction_type,amount,balance_after,transaction_id=None,timestamp=None):
        self._transation_id = transaction_id
        self._account_number = account_number
        self._transaction_type = transaction_type
        self._amount = amount
        self._balance_after = balance_after

        if timestamp:
            self._timestamp = timestamp

        else:
            self._timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_transaction_id(self):
        return self._transation_id
    
    def get_account_number(self):
        return self._account_number
    
    def get_type(self):
        return self._transaction_type
    
    def get_amount(self):
        return self._amount
    
    def get_timestamp(self):
        return self._timestamp
    
    def get_balance_after(self):
        return self._balance_after
    

    def __str__(self):
        return(
            f"[{self._timestamp}]"
            f"{self._transaction_type.upper()}"
            f"| Amount: {self._amount}"
            f"| Balance After: {self._balance_after}"

        )