'''A module for testing the middle_char module'''
import unittest
from middle_char import center_of

class TestMiddleChar(unittest.TestCase):
    '''A class for testing the middle_char module'''
    def test_three_word_phrase(self):
        '''A function to test the middle character of an odd length
           string of three words'''
        phrase = 'I love ruby'
        mid = center_of(phrase)
        self.assertEqual(mid, 'e')

    def test_two_word_phrase(self):
        '''A function to test the middle character of an odd length
           string of two words'''
        phrase = 'Launch School'
        mid = center_of(phrase)
        self.assertEqual(mid, ' ')

    def test_single_word_of_odd_length(self):
        '''A function to testt the middle characters of an even length
           string containing a single word'''
        word = 'Launch'
        mid = center_of(word)
        self.assertEqual(mid, 'un')

    def test_a_longer_word_of_odd_length(self):
        '''A function to testt the middle characters of an even length
           string containing a single word'''
        word = 'Launchschool'
        mid = center_of(word)
        self.assertEqual(mid, 'hs')

    def test_a_single_letter(self):
        '''A function to test the middle character of a single
           letter'''
        letter = 'x'
        mid = center_of(letter)
        self.assertEqual(mid, 'x')


if __name__ == '__main__':
    unittest.main()
