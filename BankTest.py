import unittest

from oop1.bank import Bank

from oop1.exceptions import InsufficientFundsException


class BankTest(unittest.TestCase):
    def test_register_customer(self):
        bank = Bank("Gtb Bank")
        bank.register_customer("Bally", "Sulaiman", "1234")
        self.assertEqual(1, bank.get_accounts())

    def test_find_account(self):
        bank = Bank("Gtb Bank")
        found_account = bank.register_customer("Bally", "Sulaiman", "1234")
        self.assertEqual(1, bank.get_accounts())
        self.assertEqual(found_account, bank.find_account(101))
        self.assertEqual("Bally Sulaiman", found_account.get_name())

    def test_deposit(self):
        bank = Bank("Gtb Bank")
        account = bank.register_customer("Esther", "Tobiloba", "1234")
        bank.deposit(account.get_number(), 1000)
        self.assertEqual(1000, account.get_balance())

    def test_deposit_twice(self):
        bank = Bank("Gtb Bank")
        account = bank.register_customer("Praise", "Oyewole", "1245")
        bank.deposit(account.get_number(), 5000)
        bank.deposit(account.get_number(), 4000)
        self.assertEqual(9000, account.get_balance())

    def test_withdraw_negative_amount_balance_remains_unchanged(self):
        bank = Bank("Gtb Bank")
        account = bank.register_customer("Esther", "Tobiloba", "1234")
        with self.assertRaises(InsufficientFundsException):
            bank.withdraw(account.get_number(), -1000, "1234")

    def test_withdraw_amount_greater_than_balance_throws_insufficient_funds_exception(self):
        bank = Bank("Gtb Bank")
        account = bank.register_customer("Esther", "Tobiloba", "1234")
        bank.deposit(account.get_number(), 500)
        with self.assertRaises(InsufficientFundsException):
            bank.withdraw(account.get_number(), 1000, "1234")
        self.assertEqual(500, account.get_balance())

    def test_withdraw(self):
        bank = Bank("Gtb Bank")
        account = bank.register_customer("Esther", "Tobiloba", "1234")
        bank.deposit(account.get_number(), 2000)
        bank.withdraw(account.get_number(), 1000, "1234")
        self.assertEqual(1000, account.get_balance())

    def test_check_balance(self):
        bank = Bank("Gtb Bank")
        account = bank.register_customer("Bally", "Sulaiman", "1234")
        bank.check_balance(account.get_number(), "1234")
        self.assertEqual(0, account.get_balance())

    def test_remove_account(self):
        bank = Bank("Gtb Bank")
        account = bank.register_customer("Bally", "Sulaiman", "1234")
        self.assertEqual(1, bank.get_accounts())
        bank.remove_account(account.get_number(), "1234")
        self.assertEqual(0, bank.get_accounts())

    def test_deposit_1k_transfer_500_my_balance_remains_500(self):
        bank = Bank("Gtb Bank")
        account1 = bank.register_customer("firstName", "LastName", "1234")
        account2 = bank.register_customer("firstName", "LastName", "5678")
        bank.deposit(account1.get_number(), 1000)

        bank.transfer(account1.get_number(), account2.get_number(), 500, "1234")
        self.assertEqual(500, account1.get_balance())
        self.assertEqual(500, account2.get_balance())
