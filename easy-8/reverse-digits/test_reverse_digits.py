'''A module for testing the reverse_digits module'''
import unittest
from reverse_digits import reversed_number

class TestReverseDigits(unittest.TestCase):
    '''A class for testing the reverse_digits module'''
    def test_one_two_three_four_five(self):
        '''Test a five digit number 12345'''
        num = 12345
        backwards = reversed_number(num)
        self.assertEqual(backwards, 54321)

    def test_another_five_digit_number(self):
        '''Test a five digit number 12213'''
        num = 12213
        backwards = reversed_number(num)
        self.assertEqual(backwards, 31221)

    def test_a_three_digit_number(self):
        '''Test a three digit number 456'''
        num = 456
        backwards = reversed_number(num)
        self.assertEqual(backwards, 654)

    def test_twelve_thousand(self):
        '''Test the number 12000'''
        num = 12000
        backwards = reversed_number(num)
        self.assertEqual(backwards, 21)

    def test_one(self):
        '''Test the number one'''
        num = 1
        backwards = reversed_number(num)
        self.assertEqual(backwards, 1)


if __name__ == '__main__':
    unittest.main()
