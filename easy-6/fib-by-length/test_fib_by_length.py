'''A module for testing working with the fibonacci series'''
import unittest
from fib_by_length import find_fibonacci_index_by_length

class TestFibByLength(unittest.TestCase):
    '''A Class to test finiding index of a given length of a
       fibonacci number'''

    def test_two(self):
        '''Test two digit number'''
        num_len = 2
        idx = find_fibonacci_index_by_length(num_len)
        self.assertEqual(idx, 7)

    def test_three(self):
        '''Test three digit number'''
        num_len = 3
        idx = find_fibonacci_index_by_length(num_len)
        self.assertEqual(idx, 12)

    def test_ten(self):
        '''Test ten digit number'''
        num_len = 10
        idx = find_fibonacci_index_by_length(num_len)
        self.assertEqual(idx, 45)

    def test_one_hundred(self):
        '''Test one hundred digit number'''
        num_len = 100
        idx = find_fibonacci_index_by_length(num_len)
        self.assertEqual(idx, 476)

    @unittest.skip("Too big of a number to handle recursively")
    def test_one_thousand(self):
        '''Test one thousand digit number'''
        num_len = 1000
        idx = find_fibonacci_index_by_length(num_len)
        self.assertEqual(idx, 4782)

    @unittest.skip("Too big of a number to handle recursively")
    def test_ten_thousand(self):
        '''Test ten thousand digit number'''
        num_len = 10_000
        idx = find_fibonacci_index_by_length(num_len)
        self.assertEqual(idx, 47847)


if __name__ == '__main__':
    unittest.main()
