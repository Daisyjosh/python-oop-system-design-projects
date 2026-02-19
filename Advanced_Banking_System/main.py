from services.bank import Bank


def main():
    bank = Bank()

    while True:
        print("\n===== Advanced Banking System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Show Passbook")
        print("6. Apply Interest (Savings Only)")
        print("7. Freeze Account")
        print("8. Activate Account")
        print("9. Delete Account")
        print("10. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter account holder name: ")
                acc_type = input("Enter account type (savings/current): ")
                balance = float(input("Enter initial balance: "))

                account = bank.create_account(name, acc_type, balance)
                print(f"Account created successfully. Account Number: {account.get_account_number()}")

            elif choice == "2":
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                new_balance = bank.deposit(acc_no, amount)
                print(f"Deposit successful. New Balance: {new_balance}")

            elif choice == "3":
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                new_balance = bank.withdraw(acc_no, amount)
                print(f"Withdrawal successful. New Balance: {new_balance}")

            elif choice == "4":
                sender = int(input("Enter sender account number: "))
                receiver = int(input("Enter receiver account number: "))
                amount = float(input("Enter transfer amount: "))
                result = bank.transfer(sender, receiver, amount)
                print(result)

            elif choice == "5":
                acc_no = int(input("Enter account number: "))
                bank.show_passbook(acc_no)

            elif choice == "6":
                acc_no = int(input("Enter savings account number: "))
                result = bank.apply_interest(acc_no)
                print(result)

            elif choice == "7":
                acc_no = int(input("Enter account number: "))
                bank.freeze_account(acc_no)
                print("Account frozen successfully.")

            elif choice == "8":
                acc_no = int(input("Enter account number: "))
                bank.activate_account(acc_no)
                print("Account activated successfully.")

            elif choice == "9":
                acc_no = int(input("Enter account number: "))
                result = bank.delete_account(acc_no)
                print(result)

            elif choice == "10":
                print("Exiting system.")
                bank.db.close()
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()