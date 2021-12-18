'''A module to test staggered_caps module for string case manipulation
   '''
import unittest
from staggered_caps import staggered_caps

class TestStaggeredCaps(unittest.TestCase):
    '''A class to test staggered_caps module for string case
       manipulation'''
    def test_string_of_alphas_and_special_characters_with_whitespace(self):
        '''Test a string with alpha, special, and whitespace chars'''
        phrase = 'I Love Launch School!'
        staggered = staggered_caps(phrase)
        self.assertEqual(staggered, 'I LoVe lAuNcH ScHoOl!')

    def test_all_caps_and_special_char_string(self):
        '''Test a string with all uppercase alpha and special chars'''
        all_caps = 'ALL_CAPS'
        staggered = staggered_caps(all_caps)
        self.assertEqual(staggered, 'AlL_CaPs')

    def test_alphas_whitespace_and_numbers(self):
        '''Test a string with alphanumeric and whitespace chars'''
        alphanum = 'ignore 77 the 444 numbers'
        staggered = staggered_caps(alphanum)
        self.assertEqual(staggered, 'IgNoRe 77 ThE 444 NuMbErS')


if __name__ == '__main__':
    unittest.main()
