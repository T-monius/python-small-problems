import unittest
from palindromic_strings import (is_palindrome,
    is_real_palindrome,
    is_palindromic_number)

class TestPalindromicStrings(unittest.TestCase):
	def test_single_palindrome(self):
		word = 'madam'
		result = is_palindrome(word)
		self.assertTrue(result)


	def test_palindromic_word_wrong_case(self):
		word = 'Madam'
		result = is_palindrome(word)
		self.assertFalse(result)


	def test_palindromic_phrase_with_punctuation(self):
		phrase = "madam i'm adam"
		result = is_palindrome(phrase)
		self.assertFalse(result)


	def test_palindromic_number(self):
		num = '356653'
		result = is_palindrome(num)
		self.assertTrue(result)


	def test_single_palindrome(self):
		word = 'madam'
		result = is_real_palindrome(word)
		self.assertTrue(result)


	def test_again_palindromic_word_wrong_case(self):
		word = 'Madam'
		result = is_real_palindrome(word)
		self.assertTrue(result)


	def test_again_palindromic_phrase_with_punctuation(self):
		phrase = "madam i'm adam"
		result = is_real_palindrome(phrase)
		self.assertTrue(result)		


	def test_again_palindromic_number(self):
		num = '356653'
		result = is_real_palindrome(num)
		self.assertTrue(result)


	def test_palindromic_numbers_and_alpha(self):
		salmple_str = '356a653'
		result = is_real_palindrome(salmple_str)
		self.assertTrue(result)


	def test_non_palindromic_numbers_and_alpha(self):
		salmple_str = '123ab321'
		result = is_real_palindrome(salmple_str)
		self.assertFalse(result)


	def test_five_digit_number(self):
		num = 34543
		result = is_palindromic_number(num)
		self.assertTrue(result)


	def test_six_digit_number(self):
		num = 123210
		result = is_palindromic_number(num)
		self.assertFalse(result)


	def test_two_digit_number(self):
		num = 22
		result = is_palindromic_number(num)
		self.assertTrue(result)


	def test_the_number_five(self):
		num = 5
		result = is_palindromic_number(num)
		self.assertTrue(result)



if __name__ == '__main__':
	unittest.main()