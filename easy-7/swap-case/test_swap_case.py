'''A module for testing swapping letter cases with swape_case module'''
import unittest
from swap_case import swapcase

class TestSwapCase(unittest.TestCase):
    '''A class to test swap_case module'''
    def test_a_cammel_case_word(self):
        '''Test a single word that is camel case'''
        word = 'CamelCase'
        swapped = swapcase(word)
        self.assertEqual(swapped, 'cAMELcASE')

    def test_phrase_with_alphas_and_non_alphas(self):
        '''Test a phrase with alpha and non-alpha characters'''
        phrase = 'Tonight on XYZ-TV'
        swapped = swapcase(phrase)
        self.assertEqual(swapped, 'tONIGHT ON xyz-tv')


if __name__ == '__main__':
    unittest.main()
