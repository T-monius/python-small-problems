'''A module for testing the double_char module'''
import unittest
from double_char import repeater, double_consonants

class TestDoubleChar(unittest.TestCase):
    '''A class for testing the double_char module'''
    def test_single_word(self):
        '''Double the characters of an all alpha word'''
        word = 'Hello'
        doubled = repeater(word)
        self.assertEqual(doubled, 'HHeelllloo')

    def test_two_words_and_special_char(self):
        '''Test a string with two words and special characters'''
        phrase = 'Good job!'
        doubled = repeater(phrase)
        self.assertEqual(doubled, 'GGoooodd  jjoobb!!')

    def test_an_empty_string(self):
        '''Test doubling and empty string'''
        empty = ''
        doubled = repeater(empty)
        self.assertEqual(doubled, '')

    def test_word_only_consonants(self):
        '''Double consonant characters of an all alpha string'''
        word = 'String'
        doubled = double_consonants(word)
        self.assertEqual(doubled, 'SSttrrinngg')

    def test_alpha_and_special_chars_only_consonants(self):
        '''Double only consonants of a string of alpha and special
           characters'''
        target = 'Hello-World!'
        doubled = double_consonants(target)
        self.assertEqual(doubled, 'HHellllo-WWorrlldd!')

    def test_phrase_only_consonants(self):
        '''Test a short phrase with numeric and whitespace'''
        phrase = 'July 4th'
        doubled = double_consonants(phrase)
        self.assertEqual(doubled, 'JJullyy 4tthh')

    def test_an_empty_string_only_consonants(self):
        '''Double only the consonants of an empty string'''
        empty = ''
        doubled = double_consonants(empty)
        self.assertEqual(doubled, '')


if __name__ == '__main__':
    unittest.main()
