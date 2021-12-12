'''A module for testing find_duplicate module'''
import unittest
from find_duplicate import find_dup

class TestFindDuplicate(unittest.TestCase):
    '''A class for testing whether a duplicate was found in a list'''
    def test_small_list(self):
        '''Test a small list'''
        nums = [7, 2, 22, 5, 5, 6, 3]
        dup = find_dup(nums)
        self.assertEqual(dup, 5)

    def test_larger_list(self):
        '''Test a larger list'''
        nums = [18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
          38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
          14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
          78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
          89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
          41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
          55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
          85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
          40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
          7,  34, 57, 74, 45, 11, 88, 67,  5, 58]
        dup = find_dup(nums)
        self.assertEqual(dup, 73)


if __name__ == '__main__':
    unittest.main()[7, 2, 22, 5, 5, 6, 3]
