from data.database_handler import DatabaseHandler
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from models.transaction import Transaction

class Bank:
    def __init__(self):
        self.db = DatabaseHandler()

    def create_account(self,account_holder,account_type,initial_balance):
        account_number = self.db.create_account(account_holder,account_type,initial_balance)
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number,account_holder,initial_balance)
        elif account_type.lower() == "current":
            account = CurrentAccount(account_number,account_holder,initial_balance)
        else:
            raise Exception("Invalid account type")
        
        return account
    
    def get_account(self,account_number):
        row = self.db.get_account(account_number)

        if not row:
            raise ValueError("Account not found.")
        
        acc_no, holder, acc_type, balance, status = row
        if acc_type.lower() == "savings":
            return SavingsAccount(acc_no,holder,balance,status)
        elif acc_type.lower() == "current":
            return CurrentAccount(acc_no,holder,balance,status) 
        else:
            raise ValueError("Unknown account type.")
        

    def deposit(self,account_number,amount):
        account = self.get_account(account_number)
        new_balance = account.deposit(amount)
        self.db.update_balance(account_number,new_balance)

        transaction = Transaction(account_number,"deposit",amount,new_balance)

        self.db.add_transaction(transaction.get_account_number(),transaction.get_type(),transaction.get_amount(),transaction.get_balance_after())

        return new_balance
    
    def withdraw(self,account_number,amount):
        account = self.get_account(account_number)
        new_balance = account.withdraw(amount)
        self.db.update_balance(account_number,new_balance)

        transaction = Transaction(
            account_number,"withdraw",amount,new_balance
        )

        self.db.add_transaction(transaction.get_account_number(),transaction.get_type(),transaction.get_amount(),transaction.get_balance_after())
        return new_balance
    
    def transfer(self,sender_acc_no,receiver_acc_no,amount):
        if sender_acc_no == receiver_acc_no:
            raise ValueError("Cannot transfer to the same account")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        
        try:
            self.db.connection.execute("BEGIN")

            sender = self.get_account(sender_acc_no)
            receiver = self.get_account(receiver_acc_no)

            new_sender_balance = sender.withdraw(amount)
            new_receiver_balance = receiver.deposit(amount)

            self.db.update_balance(sender_acc_no,new_sender_balance)
            self.db.update_balance(receiver_acc_no,new_receiver_balance)

            sender_transaction = Transaction(sender_acc_no,"transfer_out",amount,new_sender_balance)
            receiver_transaction = Transaction(receiver_acc_no,"transfer in",amount,new_receiver_balance)

            self.db.add_transaction(
                sender_transaction.get_account_number(),
                sender_transaction.get_type(),
                sender_transaction.get_amount(),
                sender_transaction.get_balance_after()
            )

            self.db.add_transaction(
                receiver_transaction.get_account_number(),
                receiver_transaction.get_type(),
                receiver_transaction.get_amount(),
                receiver_transaction.get_balance_after()
            )

            self.db.connection.commit()

            return "Transfer Successful."
        
        except Exception as e:
            self.db.connection.rollback()
            raise e
    def show_passbook(self,account_number):
        transactions = self.db.get_transaction(account_number)

        if not transactions:
            print("No transactions found")
            return
        
        for row in transactions:
            transaction_id, acc_no, t_type, amount, timestamp, balance_after = row
            transaction = Transaction(
                acc_no, t_type,amount,balance_after,transaction_id = transaction_id,timestamp=timestamp
            )

            print(transaction)
    def delete_account(self, account_number):
        self.db.delete_transactions(account_number)
        self.db.delete_account(account_number)
        return "Account deleted successfully."
    
    def freeze_account(self, account_number):
        self.db.cursor.execute("""
        UPDATE accounts SET status = 'FROZEN' WHERE account_number = ?
        """, (account_number,))
        self.db.connection.commit()
        
    def activate_account(self, account_number):
        self.db.cursor.execute("""
        UPDATE accounts SET status = 'ACTIVE' WHERE account_number = ?
        """, (account_number,))
        self.db.connection.commit()
    
