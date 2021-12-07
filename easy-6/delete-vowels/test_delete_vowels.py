import unittest
from delete_vowels import remove_vowels

class TestDeleteVowels(unittest.TestCase):
    '''Test delete_vowels module removes vowels from lists of words'''
    def test_abcs(self):
        '''Remove vowels from the abcs'''
        words = ['abcdefghijklmnopqrstuvwxyz']
        no_vowels = remove_vowels(words)
        self.assertEqual(no_vowels, ['bcdfghjklmnpqrstvwxyz'])

    def test_colors(self):
        '''Remove vowels from a list of colors, case-insensitive'''
        colors = ['green', 'YELLOW', 'black', 'white']
        no_vowels = remove_vowels(colors)
        self.assertEqual(no_vowels, ['grn', 'YLLW', 'blck', 'wht'])

    def test_capitals(self):
        '''Test all capital letters'''
        caps = ['ABC', 'AEIOU', 'XYZ']
        no_vowels = remove_vowels(caps)
        self.assertEqual(no_vowels, ['BC', '', 'XYZ'])


if __name__ == '__main__':
    unittest.main()
