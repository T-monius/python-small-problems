'''A module for testing the counting_up module'''
import unittest
from counting_up import sequence

class TestCountingUp(unittest.TestCase):
    '''A class for testing the counting_up module'''
    def test_five(self):
        '''Test the input number 5'''
        num = 5
        numbers = sequence(num)
        self.assertEqual(numbers, [1, 2, 3, 4, 5])

    def test_three(self):
        '''Test the input number 3'''
        num = 3
        numbers = sequence(num)
        self.assertEqual(numbers, [1, 2, 3])

    def test_one(self):
        '''Test the input number 1'''
        num = 1
        numbers = sequence(num)
        self.assertEqual(numbers, [1])


if __name__ == '__main__':
    unittest.main()
