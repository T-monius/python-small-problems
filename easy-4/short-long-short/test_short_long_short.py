import unittest
from short_long_short import short_long_short

class TestShortLongShort(unittest.TestCase):
	def test_abcs(self):
		string_zero = 'abc'
		string_one = 'defgh'
		concatenation = short_long_short(string_zero, string_one)
		self.assertEqual(concatenation, 'abcdefghabc')


	def test_more_abcs(self):
		string_zero = 'abcde'
		string_one = 'fgh'
		concatenation = short_long_short(string_zero, string_one)
		self.assertEqual(concatenation, 'fghabcdefgh')


	def test_one_empty_string_and_and_a_non_empty_string(self):
		string_zero = ''
		string_one = 'xyz'
		concatenation = short_long_short(string_zero, string_one)
		self.assertEqual(concatenation, 'xyz')


if __name__ == '__main__':
	unittest.main()
