'''A module to test the sum_square_sum module'''
import unittest
from sum_square_sum import sum_square_difference

class TestSumSquareSum(unittest.TestCase):
    '''A class to test the sum_square_sum module'''
    def test_three(self):
        '''Test the positive integers from up to three inclusive'''
        num = 3
        difference = sum_square_difference(num)
        self.assertEqual(difference, 22)


    def test_ten(self):
        '''Test the positive integers from up to ten inclusive'''
        num = 10
        difference = sum_square_difference(num)
        self.assertEqual(difference, 2640)


    def test_one(self):
        '''Test the positive integers from up to one inclusive'''
        num = 1
        difference = sum_square_difference(num)
        self.assertEqual(difference, 0)


    def test_one_hundred(self):
        '''Test the positive integers from up to one hundred
           inclusive'''
        num = 100
        difference = sum_square_difference(num)
        self.assertEqual(difference, 25_164_150)


if __name__ == '__main__':
    unittest.main()
