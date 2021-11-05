import unittest
from square_an_argument import square

class TestSquareAnArgument(unittest.TestCase):
    def test_five(self):
        integer = 5
        desired_square = 25
        result = square(5)
        self.assertEqual(result, desired_square)

    def test_negative_eight(self):
        integer = -8
        desired_square = 64
        result = square(integer)
        self.assertEqual(result, desired_square)

if __name__ == '__main__':
    unittest.main()