import unittest
from sevensegment import SevenSegment


class TestSevenSegment(unittest.TestCase):

    def setUp(self):
        self.sevensegment = SevenSegment()
        self.sevensegment.turn_on()

    def test_check_if_it_on(self):
        self.assertTrue(self.sevensegment.is_on)

    def test_input(self):
        self.sevensegment.splitting_into_array("1111110")

    def test_input1(self):
        self.sevensegment.splitting_into_array("0110000")

    def test_input2(self):
        self.sevensegment.splitting_into_array("1101101")

    def test_input3(self):
        self.sevensegment.splitting_into_array("1111001")

    def test_input4(self):
        self.sevensegment.splitting_into_array("0110011")

    def test_input5(self):
        self.sevensegment.splitting_into_array("1011011")

    def test_input6(self):
        self.sevensegment.splitting_into_array("1011111")

    def test_input7(self):
        self.sevensegment.splitting_into_array("1110000")

    def test_input8(self):
        self.segments = ["1", "1", "1", "1", "1", "1", "1"]
        self.sevensegment.splitting_into_array("1111111")

    def test_input9(self):
        self.sevensegment.splitting_into_array("1110011")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.assertEqual(7, self.sevensegment.splitting_into_array("0111111111"))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            self.assertEqual(7, self.sevensegment.splitting_into_array("23313111111"))


if __name__ == '__main__':
    unittest.main()
