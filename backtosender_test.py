from backtosender import BackToSender
from unittest import TestCase


class TestBackToSenderFunction(TestCase):
    def setUp(self):
        self.back_to_sender = BackToSender()

    def test_when_collection_rate_is_above_70_percentage(self):
        percentage_rate = self.back_to_sender.percentage_rate(80)
        rider_daily_wage = self.back_to_sender.calculate_daily_wage(percentage_rate)
        self.assertEqual(45000, rider_daily_wage)

    def test_when_collection_rate_is_less_than_50_percentage(self):
        percentage_rate = self.back_to_sender.percentage_rate(25)
        rider_daily_wage = self.back_to_sender.calculate_daily_wage(percentage_rate)
        self.assertEqual(9000, rider_daily_wage)

    def test_collection_rate_is_above_the_rate_raise_ValueError(self):
        with self.assertRaises(ValueError):
            self.back_to_sender.calculate_daily_wage(120)

    def test_collection_rate_is_lesser_than_0_raise_ValueError(self):
        with self.assertRaises(ValueError):
            self.back_to_sender.calculate_daily_wage(-50)