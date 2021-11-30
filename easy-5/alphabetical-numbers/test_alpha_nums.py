'''
A module for testing alpha_nums module which works with integers
according to their English word value
'''
import unittest
from alpha_nums import alphabetic_number_sort

class TestAlphaNums(unittest.TestCase):
    '''A class for testing alpha_nums module which works with
       integers according to their English word value'''
    def test_zero_to_nineteen(self):
        '''
        Test the list of numbers from zero to nineteen to be ordered
        by their English counterpart
        '''
        zero_to_nineteen = list(range(0, 20))
        ordered_nums = alphabetic_number_sort(zero_to_nineteen)
        proper_english_order = [
            8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17,
            6, 16, 10, 13, 3, 12, 2, 0,
        ]
        self.assertEqual(ordered_nums, proper_english_order)


if __name__ == '__main__':
    unittest.main()
