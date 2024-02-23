import unittest
from oop1.account import Account
from oop1.exceptions import InvalidAmountException, InsufficientFundsException


class AccountTest(unittest.TestCase):
    def test_deposit_negative_balance_remains_unchanged(self):
        account = Account("name", "1234", 1)
        with self.assertRaises(InvalidAmountException):
            account.deposit(-50_000)

    def test_deposit_positive_amount_balance_increase(self):
        account = Account("name", "1234", 0)
        self.assertEqual(0, account.get_balance())
        account.deposit(2_000)
        self.assertEqual(2_000, account.get_balance())

    def test_deposit_positive_amount_twice_balance_increase(self):
        account = Account("name", "1234", 0)
        self.assertEqual(0, account.get_balance())
        account.deposit(2_000)
        account.deposit(4_000)
        self.assertEqual(6_000, account.get_balance())

    def test_withdraw_negative_amount_balance_remains_unchanged(self):
        account = Account("name", "1234", 1)
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(-50_000, "1234")
        self.assertEqual(0, account.get_balance())

    def test_withdraw_positive_balance(self):
        account = Account("name", "1234", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(1200)
        account.withdraw(1000, "1234")
        self.assertEqual(200, account.get_balance())

    def test_withdraw_negative_balance_balance_remains_unchanged(self):
        account = Account("name", "1234", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(200)
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(-50_000, "1234")
        self.assertEqual(200, account.get_balance())

    def test_withdraw_negative_balance_twice_balance_remains_unchanged(self):
        account = Account("name", "1234", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(200)
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(-1_000, "1234")
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(-5_000, "1234")
        self.assertEqual(200, account.get_balance())

    def test_check_account_balance(self):
        account = Account("name", "1234", 0)
        account.check_balance("1234")
        self.assertEqual(0, account.get_balance())

    def test_check_account_balance_after_deposit_account_balance_change(self):
        account = Account("name", "1234", 0)
        account.deposit(1_000)
        account.check_balance("1234")
        self.assertEqual(1_000, account.get_balance())


if __name__ == '__main__':
    unittest.main()
