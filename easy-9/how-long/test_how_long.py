'''A module for testing the how_long module for generating information
   about lengths of words in a string'''
import unittest
from how_long import word_lengths

class TestHowLong(unittest.TestCase):
    '''A class for testing the how_long module for generating information
       about lengths of words in a string'''
    def test_three_words(self):
        '''Test a three word string'''
        src = 'cow sheep chicken'
        lengths = word_lengths(src)
        self.assertEqual(lengths, ["cow 3", "sheep 5", "chicken 7"])

    def test_six_words(self):
        '''Test a six word srtring'''
        src = "baseball hot dogs and apple pie"
        lengths = word_lengths(src)
        self.assertEqual(lengths, [
            "baseball 8",
            "hot 3",
            "dogs 4",
            "and 3",
            "apple 5",
            "pie 3"])

    def test_five_words(self):
        '''Test a five word string'''
        src = "It ain't easy, is it?"
        lengths = word_lengths(src)
        self.assertEqual(lengths, [
            "It 2",
            "ain't 5",
            "easy, 5",
            "is 2",
            "it? 3"])

    def test_one_long_word(self):
        '''Test a single word that is quite long'''
        word = "Supercalifragilisticexpialidocious"
        lengths = word_lengths(word)
        self.assertEqual(lengths, ["Supercalifragilisticexpialidocious 34"])


if __name__ == '__main__':
    unittest.main()
