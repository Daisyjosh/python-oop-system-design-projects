import sqlite3
from datetime import datetime


class DatabaseHandler:
    def __init__(self):
        self.connection = sqlite3.connect("banking.db")
        self.cursor = self.connection.cursor()
        self.create_tables() # creates table if doesn't exists

    
    # Creating tables
    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY AUTOINCREMENT,
            account_holder TEXT NOT NULL,
            account_type TEXT NOT NULL,
            balance REAL NOT NULL,
            status TEXT NOT NULL
            )

        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp TEXT NOT NULL,
            balance_after REAL NOT NULL,
            FOREIGN KEY (account_number) REFERENCES accounts(account_number)
            )

        """)

        self.connection.commit()
    
    # create account
    def create_account(self,account_holder,account_type,balance,status="ACTIVE"):
        self.cursor.execute("""
            INSERT INTO accounts(account_holder,account_type,balance,status) VALUES (?,?,?,?)
        """,(account_holder,account_type,balance,status))
        
        self.connection.commit()
        return self.cursor.lastrowid
    
    # get account details
    def get_account(self,account_number):
        self.cursor.execute("""
            SELECT * FROM accounts WHERE account_number = ?
        """,(account_number,))
        return self.cursor.fetchone()


    # update_balance
    def update_balance(self,account_number,new_balance):
        self.cursor.execute("""
        UPDATE accounts SET balance = ? WHERE account_number = ?
        """,(new_balance,account_number))

        self.connection.commit()

    # delete an account
    def delete_account(self,account_number):
        self.cursor.execute("""
        DELETE FROM accounts WHERE account_number = ?
        """,(account_number))

        self.connection.comit()

    # add transation
    def add_transaction(self,account_number,transaction_type,amount,balance_after):
        timestamp = datetime().now.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
            INSERT INTO transactions (account_number,account_type,amount,balance_after,timestamp) VALUES (?,?,?,?,?)
        """,(account_number,transaction_type,amount,balance_after,timestamp))
        self.connection.commit()

    # get transaction
    def get_transaction(self,account_number):
        self.cursor.execute("""
            SELECT * FROM transactions WHERE account_number = ?
            ORDER BY transaction_id
        """,(account_number,))
        return self.cursor.fetchall()

    def delete_transactions(self, account_number):
        self.cursor.execute("""
        DELETE FROM transactions WHERE account_number = ?
        """, (account_number,))
        self.connection.commit()
    
    def close(self):
        self.connection.close()

    
    

        