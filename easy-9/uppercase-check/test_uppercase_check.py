'''A module for testing the uppercase_check module'''
import unittest
from uppercase_check import is_uppercase

class TestUppercaseCheck(unittest.TestCase):
    '''A class for testing the uppercase_check module'''
    def test_a_single_lowercase_alpha(self):
        '''Test a string containing the single alpha character "t"'''
        letter = 't'
        result = is_uppercase(letter)
        self.assertFalse(result)

    def test_a_single_uppercase_alpha(self):
        '''Test a string containing the single alpha character "T"'''
        letter = 'T'
        result = is_uppercase(letter)
        self.assertTrue(result)

    def test_a_phrase_with_lowercase_letters(self):
        '''Test a phrase containing lowercase characters'''
        letter = 'Four Score'
        result = is_uppercase(letter)
        self.assertFalse(result)

    def test_a_phrase_whose_alphase_are_uppercase(self):
        '''Test a string whose alpha characters are all uppercase'''
        letter = 'FOUR SCORE'
        result = is_uppercase(letter)
        self.assertTrue(result)

    def test_another_phrase_whose_alphase_are_uppercase(self):
        '''Test another string whose alpha characters are all
           uppercase'''
        letter = '4SCORE!'
        result = is_uppercase(letter)
        self.assertTrue(result)

    def test_an_empty_string(self):
        '''Test an empty string'''
        letter = ''
        result = is_uppercase(letter)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
