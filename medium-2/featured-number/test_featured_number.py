'''A module to test the featured_number module'''
import unittest
from featured_number import next_featured_num, next_multiple_of_seven, is_all_unique_digits

class TestFeaturedNumber(unittest.TestCase):
    '''A class to test the featured_nuber module'''
    def test_next_multiple_of_7_after_12(self):
        '''Find the next multiple of seven after the number 12'''
        num = 12
        next_multiple = next_multiple_of_seven(num)
        self.assertEqual(next_multiple, 14)


    def test_all_unique_digits(self):
        '''Confirm that a number has all unique digits'''
        num = 12
        is_all_unique = is_all_unique_digits(num)
        self.assertTrue(is_all_unique)


    def test_not_all_unique_digits(self):
        '''Confirm that a number does not have all unique digits'''
        num = 22
        is_all_unique = is_all_unique_digits(num)
        self.assertFalse(is_all_unique)


    def test_twelve(self):
        '''Find the next featured number after 12'''
        num = 12
        result = next_featured_num(num)
        self.assertEqual(result, 21)


    def test_twenty(self):
        '''Find the next featured number after 20'''
        num = 20
        result = next_featured_num(num)
        self.assertEqual(result, 21)


    def test_twenty_one(self):
        '''Find the next featured number after 21'''
        num = 21
        result = next_featured_num(num)
        self.assertEqual(result, 35)


    def test_nine_ninety_seven(self):
        '''Find the next featured number after 997'''
        num = 997
        result = next_featured_num(num)
        self.assertEqual(result, 1029)


    def test_a_thousand_twenty_nine(self):
        '''Find the next featured number after 1029'''
        num = 1029
        result = next_featured_num(num)
        self.assertEqual(result, 1043)


    def test_almost_a_million(self):
        '''Find the next featured number after 999_999'''
        num = 999_999
        result = next_featured_num(num)
        self.assertEqual(result, 1_023_547)


    def test_almost_a_billion(self):
        '''Find the next featured number after 999_999_987'''
        num = 999_999_987
        result = next_featured_num(num)
        self.assertEqual(result, 1_023_456_987)


    def test_limit(self):
        '''Find surpassing the limit'''
        num = 9_999_999_999
        result = next_featured_num(num)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
