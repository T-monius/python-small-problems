'''A module for testing a module that works with words in strings'''
import unittest
from end_is_near import penultimate

class TestEndIsNear(unittest.TestCase):
    '''A class for testing end_is_near module'''
    def test_two_words(self):
        '''Test two words'''
        short_phrase = 'last word'
        penultimate_word = penultimate(short_phrase)
        self.assertEqual(penultimate_word, 'last')

    def test_phrase(self):
        '''Test a phrase'''
        phrase = 'Launch School is great!'
        penultimate_word = penultimate(phrase)
        self.assertEqual(penultimate_word, 'is')


if __name__ == '__main__':
    unittest.main()
