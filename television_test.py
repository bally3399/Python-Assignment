import unittest
from television import Television


class TestTelevisionFunction(unittest.TestCase):
    def setUp(self):
        self.television = Television()

    def test_tv_is_on(self):
        self.assertFalse(self.television.television_is_on())
        self.television.turn_on()
        self.assertTrue(self.television.television_is_on())

    def test_tv_is_off(self):
        self.assertFalse(self.television.television_is_on())
        self.television.turn_off()
        self.assertFalse(self.television.television_is_on())

    def test_tv_volume_increase(self):
        self.assertFalse(self.television.television_is_on())
        self.television.turn_on()
        self.assertTrue(self.television.television_is_on())
        self.assertEqual(0, self.television.get_volume())
        self.television.volume_up()
        self.assertEqual(1, self.television.get_volume())

    def test_tv_volume_cannot_increase_while_off(self):
        self.assertFalse(self.television.television_is_on())
        self.television.turn_on()
        self.assertTrue(self.television.television_is_on())
        self.assertEqual(0, self.television.get_volume())
        self.television.turn_off()
        self.assertFalse(self.television.television_is_on())
        self.television.volume_up()
        self.assertEqual(0, self.television.get_volume())

    def test_tv_volume_decrease(self):
        self.assertFalse(self.television.television_is_on())
        self.television.turn_on()
        self.assertTrue(self.television.television_is_on())
        self.assertEqual(0, self.television.get_volume())
        self.television.volume_up()
        self.television.volume_up()
        self.assertEqual(2, self.television.get_volume())
        self.television.volume_down()
        self.assertEqual(1, self.television.get_volume())

    def test_tv_volume_cannot_decrease_while_off(self):
        self.assertFalse(self.television.television_is_on())
        self.television.turn_on()
        self.assertTrue(self.television.television_is_on())
        self.assertEqual(0, self.television.get_volume())
        self.television.volume_up()
        self.television.volume_up()
        self.assertEqual(2, self.television.get_volume())
        self.television.turn_off()
        self.assertFalse(self.television.television_is_on())
        self.television.volume_down()
        self.assertEqual(2, self.television.get_volume())

    def test_tv_channel_can_change(self):
        self.assertFalse(self.television.television_is_on())
        self.television.turn_on()
        self.assertTrue(self.television.television_is_on())
        self.television.channel()
        self.assertEqual(1, self.television.get_channel())


if __name__ == '__main__':
    unittest.main()
