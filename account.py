from oop1.exceptions import InvalidAmountException, InvalidPinException, InsufficientFundsException


class InsufficientBalance(Exception):
    pass


class Account:
    def __init__(self, name, pin, number):
        self.name = name
        self.balance = 0
        self.pin = pin
        self.number = number

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise InvalidAmountException("Amount must be positive")

    def withdraw(self, amount, pin):
        if amount > 0 and amount <= self.balance:
                self.balance -= amount
        else:
            raise InsufficientFundsException("Insufficient Balance or invalid amount")

    def check_balance(self, pin):
        if self.pin == pin:
            return self.balance
        else:
            raise InvalidPinException("Enter valid pin")
