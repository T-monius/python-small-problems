'''A module to test the my_abcs module'''
import unittest
from my_abcs import is_block_word

class TestMyABCS(unittest.TestCase):
    '''A class to test the my_abcs module'''
    def test_a_block_word(self):
        '''Test a word that can be spelled with the blocks'''
        word = 'BATCH'
        result = is_block_word(word)
        self.assertEqual(result, True)

    def test_a_non_block_word(self):
        '''Test a word that cannnot be spelled with the blocks'''
        word = 'BUTCH'
        result = is_block_word(word)
        self.assertEqual(result, False)

    def test_another_block_word(self):
        '''Test a lowercase word that can be spelled with the blocks'''
        word = 'jest'
        result = is_block_word(word)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
