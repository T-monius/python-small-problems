import unittest
from stringy_string import binary_string

class TestBinaryString(unittest.TestCase):
	def test_six(self):
		num = 6
		binary_expectation = '101010'
		result = binary_string(num)
		self.assertEqual(result, binary_expectation)

	def test_nine(self):
		num = 9
		binary_expectation = '101010101'
		result = binary_string(num)
		self.assertEqual(result, binary_expectation)

	def test_four(self):
		num = 4
		binary_expectation = '1010'
		result = binary_string(num)
		self.assertEqual(result, binary_expectation)

	def test_seven(self):
		num = 7
		binary_expectation = '1010101'
		result = binary_string(num)
		self.assertEqual(result, binary_expectation)

if __name__ == '__main__':
	unittest.main()
