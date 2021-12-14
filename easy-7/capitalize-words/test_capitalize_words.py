'''A module for testing capitalize_words'''
import unittest
from capitalize_words import word_cap

class TestCapitalizeWords(unittest.TestCase):
    '''A class for testing capitalize_words'''
    def test_all_alpha_phrase(self):
        '''Test capitalizing a phrase of all alpha characters'''
        phrase = 'four score and seven'
        capitalized = word_cap(phrase)
        self.assertEqual(capitalized, 'Four Score And Seven')

    def test_another_all_alpha_phrase(self):
        '''Test capitalizing other phrase of all alpha characters'''
        phrase = 'the javaScript language'
        capitalized = word_cap(phrase)
        self.assertEqual(capitalized, 'The Javascript Language')

    def test_phrase_with_quoted_word(self):
        '''Test capitalizing a phrase with a quoted word'''
        phrase = 'this is a "quoted" word'
        capitalized = word_cap(phrase)
        self.assertEqual(capitalized, 'This Is A "quoted" Word')


if __name__ == '__main__':
    unittest.main()
