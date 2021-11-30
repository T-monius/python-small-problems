import unittest
from digit_list import digit_list

class TestDigitList(unittest.TestCase):
	def test_12345(self):
		expected_digits = [1, 2, 3, 4, 5]
		result = digit_list(12345)
		self.assertEqual(result, expected_digits)

	def test_7(self):
		expected_digits = [7]
		result = digit_list(7)
		self.assertEqual(result, expected_digits)

	def test_375290(self):
		expected_digits = [3, 7, 5, 2, 9, 0]
		result = digit_list(375290)
		self.assertEqual(result, expected_digits)

	def test_444(self):
		expected_digits = [4, 4, 4]
		result = digit_list(444)
		self.assertEqual(result, expected_digits)

if __name__ == '__main__':
	unittest.main()