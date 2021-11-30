'''A module for testing daily double which handles duplicate chars'''
import unittest
from daily_double import crunch

class TestDailyDouble(unittest.TestCase):
    '''Test `crunch` function from daily_double module'''
    def test_phrase_with_consecutive_dups(self):
        '''Test a phrase with multiple consecutive duplicates'''
        phrase = 'ddaaiillyy ddoouubbllee'
        collapsed_str = crunch(phrase)
        self.assertEqual(collapsed_str, 'daily double')

    def test_numbers_and_chars(self):
        '''Test text with consecutive duplicate numbers and letters'''
        text = '4444abcabccba'
        collapsed_str = crunch(text)
        self.assertEqual(collapsed_str, '4abcabcba')

    def test_all_g_s(self):
        '''Test a string of all one character duplicated'''
        g_s = 'ggggggggggggggg'
        collapsed_str = crunch(g_s)
        self.assertEqual(collapsed_str, 'g')

    def test_empty_str(self):
        '''Test an empty string'''
        empty_str = ''
        collapsed_str = crunch(empty_str)
        self.assertEqual(collapsed_str, '')


if __name__ == '__main__':
    unittest.main()
