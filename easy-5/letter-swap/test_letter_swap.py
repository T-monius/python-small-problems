import unittest
from letter_swap import letter_swap

class TestLetterSwap(unittest.TestCase):
    def test_long_prhrase(self):
        phrase = 'Oh what a wonderful day it is'
        swapped = letter_swap(phrase)
        self.assertEqual(swapped, 'hO thaw a londerfuw yad ti si')

    def test_single_letter(self):
        letter = 'a'
        swapped = letter_swap(letter)
        self.assertEqual(swapped, 'a')

    def test_single_word(self):
        word = 'Abcde'
        swapped = letter_swap(word)
        self.assertEqual(swapped, 'ebcdA')


if __name__ == '__main__':
    unittest.main()