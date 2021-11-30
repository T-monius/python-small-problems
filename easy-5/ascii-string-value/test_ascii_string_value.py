import unittest
from ascii_string_value import ascii_string_value

class TestASCIIStringValue(unittest.TestCase):
	def test_short_phrase(self):
		phrase = 'Four score'
		val = ascii_string_value(phrase)
		self.assertEqual(val, 984)

	def test_launch_school(self):
		name = 'Launch School'
		val = ascii_string_value(name)
		self.assertEqual(val, 1251)

	def test_a(self):
		char = 'a'
		val = ascii_string_value(char)
		self.assertEqual(val, 97)

	def test_empty_string(self):
		sample_string = ''
		val = ascii_string_value(sample_string)
		self.assertEqual(val, 0)


if __name__ == '__main__':
	unittest.main()
