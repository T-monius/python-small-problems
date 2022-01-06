'''A module for testing palindromic_substrings module'''
import unittest
from palindromic_substrings import is_palindromic, is_palindrome, palindromes

class TestPalindromicSubstrings(unittest.TestCase):
    '''A class for testing palindromic_substrings module'''

    def test_word_with_dashes_is_a_palindrome_with_is_palindrome(self):
        '''Test if the letter a is a palindrome'''
        letter = '-madam-'
        result = is_palindrome(letter)
        self.assertTrue(result)

    def test_if_letter_a_is_a_palindrome(self):
        '''Test if the letter a is a palindrome'''
        letter = 'a'
        result = is_palindromic(letter)
        self.assertFalse(result)

    def test_word_with_dashes(self):
        '''Test a word and dash characters'''
        letter = '-madam-'
        result = is_palindromic(letter)
        self.assertTrue(result)

    def test_another_word_with_dashes(self):
        '''Test another word and dash characters'''
        letter = 'am-did-ma'
        result = is_palindromic(letter)
        self.assertTrue(result)

    # @unittest.skip('Testing is_palindrome first')
    def test_alphabet_upto_d(self):
        '''Test alphabet characters up to the letter d'''
        alpha = 'abcd'
        result = palindromes(alpha)
        self.assertEqual(result, [])

    def test_word_with_two_palindromes(self):
        '''Test a word with two palindromes'''
        word = 'madam'
        result = palindromes(word)
        self.assertEqual(result, ['madam', 'ada'])

    def test_alpha_and_dash_characters(self):
        '''Test a series of alpha and dash characters'''
        word = 'hello-madam-did-madam-goodbye'
        result = palindromes(word)
        self.assertEqual(result, [
          'll', '-madam-', '-madam-did-madam-', 'madam', 'madam-did-madam', 'ada',
          'adam-did-mada', 'dam-did-mad', 'am-did-ma', 'm-did-m', '-did-', 'did',
          '-madam-', 'madam', 'ada', 'oo'
        ])

    def test_two_words(self):
        '''Test two words'''
        words = 'knitting cassettes'
        result = palindromes(words)
        self.assertEqual(result,[
          'nittin', 'itti', 'tt', 'ss', 'settes', 'ette', 'tt'
        ])


if __name__ == '__main__':
    unittest.main()
