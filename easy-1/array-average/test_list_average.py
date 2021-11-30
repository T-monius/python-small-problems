import unittest
from list_average import average

class TestListAverage(unittest.TestCase):
	def test_2_element_list(self):
		sample_list = [1, 6]
		expected_average = 3
		result = average(sample_list)
		self.assertEqual(result, expected_average)

	def test_6_element_list(self):
		sample_list = [1, 5, 87, 45, 8, 8]
		expected_average = 25
		result = average(sample_list)
		self.assertEqual(result, expected_average)

	def test_another_6_element_list(self):
		sample_list = [9, 47, 23, 95, 16, 52]
		expected_average = 40
		result = average(sample_list)
		self.assertEqual(result, expected_average)

if __name__ == '__main__':
	unittest.main()