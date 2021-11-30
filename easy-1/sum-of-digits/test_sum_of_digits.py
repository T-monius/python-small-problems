import unittest
from sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
	def test_twenty_three(self):
		sample_int = 23
		expected_sum = 5
		result = sum_of_digits(sample_int)
		self.assertEqual(result, expected_sum)

	def test_four_ninety_six(self):
		sample_int = 496
		expected_sum = 19
		result = sum_of_digits(sample_int)
		self.assertEqual(result, expected_sum)

	def test_one_to_nine(self):
		sample_int = 123_456_789
		expected_sum = 45
		result = sum_of_digits(sample_int)
		self.assertEqual(result, expected_sum)

if __name__ == '__main__':
	unittest.main()