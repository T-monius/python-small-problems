'''A module for testing the leading_substrings module'''
import unittest
from leading_substrings import leading_substrings

class TestLeadingSubstrings(unittest.TestCase):
    '''A class for testing the 'leading_substrings' module'''
    def test_three_letter_string(self):
        '''Test a string of three letters'''
        sample = 'abc'
        result = leading_substrings(sample)
        self.assertEqual(result, ['a', 'ab', 'abc'])

    def test_a_single_character(self):
        '''Test the string 'a' which is only a single character'''
        sample = 'a'
        result = leading_substrings(sample)
        self.assertEqual(result, ['a'])

    def test_five_characters(self):
        '''Test a string of five characters'''
        sample = 'xyzzy'
        result = leading_substrings(sample)
        self.assertEqual(result, ['x', 'xy', 'xyz', 'xyzz', 'xyzzy'])

    def test_empty_string(self):
        '''Test an empty string'''
        sample = ''
        result = leading_substrings(sample)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
