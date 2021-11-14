import unittest
from string_to_integer import string_to_integer

class TestStringToInteger(unittest.TestCase):
    def test_four_three_two_one(self):
        example_str = '4321'
        conversion = string_to_integer(example_str)
        self.assertEqual(conversion, 4321)

    def test_five_seven_zero(self):
        example_str = '570'
        conversion = string_to_integer(example_str)
        self.assertEqual(conversion, 570)


if __name__ == '__main__':
    unittest.main()