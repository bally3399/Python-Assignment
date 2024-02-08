import unittest
from bike import Bike


class TestBikeFunction(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_bike_is_on(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.is_on()
        self.assertTrue(self.bike.bike_is_on())

    def test_bike_is_off(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.is_off()
        self.assertFalse(self.bike.bike_is_on())

    def test_bike_can_accelerate(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.bike_is_on()
        self.assertFalse(self.bike.bike_is_on())
        self.assertEqual(1, self.bike.get_gear())
        self.assertEqual(0, self.bike.get_speed())
        self.bike.set_speed(15)
        self.assertEqual(15, self.bike.get_speed())
        self.assertEqual(1, self.bike.get_gear())
        self.bike.accelerate()
        self.assertEqual(16, self.bike.get_speed())

    def test_that_bike_can_accelerate_by_two(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.bike_is_on()
        self.assertFalse(self.bike.bike_is_on())
        self.assertEqual(1, self.bike.get_gear())
        self.assertEqual(0, self.bike.get_speed())
        self.bike.set_speed(20)
        self.assertEqual(20, self.bike.get_speed())
        self.assertEqual(2, self.bike.get_gear())
        self.bike.accelerate()
        self.assertEqual(22, self.bike.get_speed())

    def test_that_bike_can_accelerate_by_three(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.bike_is_on()
        self.assertEqual(1, self.bike.get_gear())
        self.assertEqual(0, self.bike.get_speed())
        self.bike.set_speed(32)
        self.assertEqual(32, self.bike.get_speed())
        self.assertEqual(3, self.bike.get_gear())
        self.bike.accelerate()
        self.assertEqual(35, self.bike.get_speed())

    def test_that_bike_can_accelerate_by_four(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.bike_is_on()
        self.assertEqual(1, self.bike.get_gear())
        self.assertEqual(0, self.bike.get_speed())
        self.bike.set_speed(40)
        self.assertEqual(40, self.bike.get_speed())
        self.assertEqual(4, self.bike.get_gear())
        self.bike.accelerate()
        self.assertEqual(44, self.bike.get_speed())

    def test_that_can_decelerate(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.bike_is_on()
        self.assertEqual(1, self.bike.get_gear())
        self.assertEqual(0, self.bike.get_speed())
        self.bike.set_speed(15)
        self.assertEqual(15, self.bike.get_speed())
        self.assertEqual(1, self.bike.get_gear())
        self.bike.decelerate()
        self.assertEqual(14, self.bike.get_speed())

    def test_that_can_decelerate_by_two(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.bike_is_on()
        self.assertEqual(1, self.bike.get_gear())
        self.assertEqual(0, self.bike.get_speed())
        self.bike.set_speed(20)
        self.assertEqual(20, self.bike.get_speed())
        self.assertEqual(2, self.bike.get_gear())
        self.bike.decelerate()
        self.assertEqual(18, self.bike.get_speed())

    def test_that_can_decelerate_by_three(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.bike_is_on()
        self.assertFalse(self.bike.bike_is_on())
        self.assertEqual(1, self.bike.get_gear())
        self.assertEqual(0, self.bike.get_speed())
        self.bike.set_speed(33)
        self.assertEqual(33, self.bike.get_speed())
        self.assertEqual(3, self.bike.get_gear())
        self.bike.decelerate()
        self.assertEqual(30, self.bike.get_speed())

    def test_that_can_decelerate_by_four(self):
        self.assertFalse(self.bike.bike_is_on())
        self.bike.bike_is_on()
        self.assertFalse(self.bike.bike_is_on())
        self.assertEqual(1, self.bike.get_gear())
        self.assertEqual(0, self.bike.get_speed())
        self.bike.set_speed(44)
        self.assertEqual(44, self.bike.get_speed())
        self.assertEqual(4, self.bike.get_gear())
        self.bike.decelerate()
        self.assertEqual(40, self.bike.get_speed())
