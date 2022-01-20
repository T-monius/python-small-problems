'''A class for testing the double_doubles module'''
import unittest
from double_doubles import twice

class TestDoubleDoubles(unittest.TestCase):
    '''A class for testing the double_doubles module'''
    def test_37(self):
        '''Test the number 37, an even length number that is not a double'''
        num = 37
        double = twice(num)
        self.assertEqual(double, 74)

    def test_a_double(self):
        '''Test an even length number that is two digits and the same
           when comparing slices before and after middle index (44)'''
        num = 44
        double = twice(num)
        self.assertEqual(double, 44)

    def test_a_six_digit_non_double(self):
        '''Test an even length number that is not a double'''
        num = 334433
        double = twice(num)
        self.assertEqual(double, 668866)

    def test_a_three_digit_number(self):
        '''Test a three digit number that's not a double'''
        num = 444
        double = twice(num)
        self.assertEqual(double, 888)

    def test_another_three_digit_number(self):
        '''Test another three digit number that's not a double'''
        num = 107
        double = twice(num)
        self.assertEqual(double, 214)

    def test_a_six_digit_double(self):
        '''Test a six digit number that is a double'''
        num = 103103
        double = twice(num)
        self.assertEqual(double, 103103)

    def test_a_four_digit_double(self):
        '''Test an even length four digit number who's digits are all
           the same and thus a double'''
        num = 3333
        double = twice(num)
        self.assertEqual(double, 3333)

    def test_another_four_digit_double(self):
        '''Test another even length four digit number that is a double'''
        num = 7676
        double = twice(num)
        self.assertEqual(double, 7676)

    def test_a_large_double(self):
        '''Test large number that is a double'''
        num = 123_456_789_123_456_789
        double = twice(num)
        self.assertEqual(double, 123_456_789_123_456_789)

    def test_a_single_digit(self):
        '''Test a single digit that can't be a double'''
        num = 5
        double = twice(num)
        self.assertEqual(double, 10)


if __name__ == '__main__':
    unittest.main()
