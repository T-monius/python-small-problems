import unittest
from odd import is_odd

class TestIsOdd(unittest.TestCase):
	def test_number_two(self):
		result = is_odd(2)
		self.assertFalse(result)

	def test_number_five(self):
		result = is_odd(5)
		self.assertTrue(result)

	def test_number_negatie_seventeen(self):
		result = is_odd(-17)
		self.assertTrue(result)

	def test_number_negative_eight(self):
		result = is_odd(-8)
		self.assertFalse(result)

	def test_number_zero(self):
		result = is_odd(2)
		self.assertFalse(result)

	def test_number_seven(self):
		result = is_odd(7)
		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main()