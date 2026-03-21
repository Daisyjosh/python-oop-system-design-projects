class ExpenseService:
    def __init__(self, db):
        self.db = db

    def add_expense(self, expense):
        self.db.cursor.execute("""
        INSERT INTO expenses (user_id, category, amount, date)
        VALUES (?, ?, ?, ?)
        """, (expense.user_id, expense.category, expense.amount, expense.date))
        self.db.conn.commit()

    def total_expense(self, user_id):
        self.db.cursor.execute(
            "SELECT SUM(amount) FROM expenses WHERE user_id=?",
            (user_id,)
        )
        return self.db.cursor.fetchone()[0]