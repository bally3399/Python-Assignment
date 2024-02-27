from oop1.bank import Bank
from oop1.exceptions import InvalidAmountException, InvalidPinException, InsufficientFundsException, \
    AccountNotFoundException


class BankApp:
    def __init__(self):
        self.bank = Bank("firstBank")

    def display(self):
        print("******************************************")
        print("Bank App")
        print("1.Create customer\n2. Close Account\n3. Deposit \n4.Transfer \n5.Withdraw\n6.Check balance "
              "\n7.Exit App")
        print("*******************************************")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.create_account()
        elif choice == "2":
            self.close_account()
        elif choice == "3":
            self.deposit()
        elif choice == "4":
            self.transfer()
        elif choice == "5":
            self.withdraw()
        elif choice == "6":
            self.check_balance()
        elif choice == "7":
            self.exit()
        else:
            print("Enter valid choice")
            self.display()

    def create_account(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter pin: ")
        self.bank.register_customer(first_name, last_name, pin)
        print("Customer register successfully!")
        print("Account Number: ", self.bank.get_accounts() + 1)
        self.display()

    def generate_account_number(self):
        return self.generate_account_number() + 1

    def deposit(self):
        account_number = input("Enter your account number: ")
        amount = input("Enter an amount: ")
        try:
            self.bank.deposit(int(account_number), int(amount))
            print("Amount deposited successfully!")
        except AccountNotFoundException as e:
            print(e)
        finally:
            self.display()

    def transfer(self):
        amount = input("Enter transfer amount: ")
        sender_account = input("Enter your account: ")
        receiver_account = input("Enter the receiver account number: ")
        pin = input("Enter your pin: ")
        try:
            self.bank.transfer(amount, sender_account, receiver_account, pin)
            print("Amount transferred successfully!")
        except InsufficientFundsException as e:
            print(e)
        finally:
            self.display()

    def withdraw(self):
        account = input("Enter your account number: ")
        amount = input("Enter the amount: ")
        pin = input("Enter your pin: ")
        try:
            self.bank.withdraw(int(account), int(amount), pin)
            print("Amount withdrawn successfully!")
        except InvalidAmountException as e:
            print(e)
        finally:
            self.display()

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        try:
            self.bank.check_balance(int(account_number), pin)
        except InvalidPinException as e:
            print(e)
        finally:
            self.display()

    def close_account(self):
        account_number = int(input("Enter the account number: "))
        pin = input("Enter your pin: ")
        try:
            self.bank.remove_account(account_number, pin)
            print("Account closed successfully!")
        except InvalidPinException as e:
            print(e)

    def exit(self):
        print("Exit")
        return


def main():
    bank_app = BankApp()
    bank_app.display()


if __name__ == "__main__":
    main()
