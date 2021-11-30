import unittest
from my_bonus import calculate_bonus

class TestMyBonus(unittest.TestCase):
	def test_2_grand_eight_hundred_with_bonus(self):
		salary = 2800
		is_bonus = True
		bonus = calculate_bonus(salary, is_bonus)
		self.assertEqual(bonus, 1400)

	def test_a_grand_no_bonus(self):
		salary = 1000
		is_bonus = False
		bonus = calculate_bonus(salary, is_bonus)
		self.assertEqual(bonus, 0)

	def test_50_grand_with_bonus(self):
		salary = 50_000
		is_bonus = True
		bonus = calculate_bonus(salary, is_bonus)
		self.assertEqual(bonus, 25_000)

	def test_no_salary(self):
		salary = None
		is_bonus = True
		bonus = calculate_bonus(salary, is_bonus)
		self.assertIsNone(bonus)

	def test_negative_salary(self):
		salary = -4500
		is_bonus = True
		bonus = calculate_bonus(salary, is_bonus)
		self.assertIsNone(bonus)


if __name__ == '__main__':
	unittest.main()