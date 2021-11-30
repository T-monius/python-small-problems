import unittest
from number_to_string import number_to_string, signed_int_to_str

class TestNumberToString(unittest.TestCase):
	def test_four_three_two_one(self):
		num = 4321
		number_string = number_to_string(num)
		self.assertEqual(number_string, '4321')

	def test_zero(self):
		num = 0
		number_string = number_to_string(num)
		self.assertEqual(number_string, '0')

	def test_five_thousand(self):
		num = 5000
		number_string = number_to_string(num)
		self.assertEqual(number_string, '5000')

	def test_four_three_two_one_signed(self):
		num = 4321
		signed_num_str = signed_int_to_str(num)
		self.assertEqual(signed_num_str, '+4321')

	def test_four_three_two_one_signed(self):
		num = -123
		signed_num_str = signed_int_to_str(num)
		self.assertEqual(signed_num_str, '-123')

	def test_four_three_two_one_signed(self):
		num = 0
		signed_num_str = signed_int_to_str(num)
		self.assertEqual(signed_num_str, '0')


if __name__ == '__main__':
	unittest.main()