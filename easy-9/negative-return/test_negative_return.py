'''A module for testing the negative_return module for negating numbers
   '''
import unittest
from negative_return import negative

class TestNegativeReturn(unittest.TestCase):
    '''A class for testing the negative_return module for negating
       numbers'''
    def test_a_positive_number(self):
        '''Test the positive number 5'''
        num = 5
        negated = negative(num)
        self.assertEqual(negated, -5)

    def test_a_negative_number(self):
        '''Test a negative number -3'''
        num = -3
        negated = negative(num)
        self.assertEqual(negated, num)

    def test_zero(self):
        '''Test the number zero'''
        zero = 0
        negated = negative(zero)
        self.assertEqual(negated, zero)


if __name__ == '__main__':
    unittest.main()
