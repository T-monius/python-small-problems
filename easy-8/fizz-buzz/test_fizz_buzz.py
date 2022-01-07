'''A module to test the fizzbuzz module'''
import unittest
from fizz_buzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    '''A class for testing the 'fizzbuzz' module'''
    def test_range_one_to_15_inclusive(self):
        '''Test a range of numbers from one to 15 inclusive'''
        start = 1
        end = 15
        result = fizzbuzz(start, end)
        self.assertEqual(result, [
            1, 2, 'Fizz', 4, 'Buzz',
            'Fizz', 7, 8, 'Fizz',
            'Buzz', 11, 'Fizz',
            13, 14, 'FizzBuzz'
        ])


if __name__ == '__main__':
    unittest.main()
