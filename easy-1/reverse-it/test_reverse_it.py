import unittest
from reverse_it_one import reverse_sentence
from reverse_it_two import reverse_words

class TestReverseIt(unittest.TestCase):
	def test_hello_world(self):
		phrase = 'Hello World'
		reversed_expectation = 'World Hello'
		result = reverse_sentence(phrase)
		self.assertEqual(result, reversed_expectation)

	def test_random_phrase(self):
		phrase = 'Reverse these words'
		reversed_expectation = 'words these Reverse'
		result = reverse_sentence(phrase)
		self.assertEqual(result, reversed_expectation)

	def test_empty_str(self):
		phrase = ''
		reversed_expectation = ''
		result = reverse_sentence(phrase)
		self.assertEqual(result, reversed_expectation)

	def test_all_spaces(self):
		phrase = '     '
		reversed_expectation = ''
		result = reverse_sentence(phrase)
		self.assertEqual(result, reversed_expectation)

	def test_reverse_words_single_long_word(self):
		phrase = 'Professional'
		reversed_expectation = 'lanoisseforP'
		result = reverse_words(phrase)
		self.assertEqual(result, reversed_expectation)

	def test_reverse_mixed_phrase(self):
		phrase = 'Walk around the block'
		reversed_expectation = 'Walk dnuora the kcolb'
		result = reverse_words(phrase)
		self.assertEqual(result, reversed_expectation)

	def test_reverse_words_launch_school(self):
		phrase = 'Launch School'
		reversed_expectation = 'hcnuaL loohcS'
		result = reverse_words(phrase)
		self.assertEqual(result, reversed_expectation)

if __name__ == '__main__':
	unittest.main()