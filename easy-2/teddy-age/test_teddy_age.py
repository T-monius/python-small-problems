import unittest
from teddy_age import how_old

class TestTeddyAge(unittest.TestCase):
	def testIsAString(self):
		result = how_old()
		print(result)
		self.assertIsInstance(result, str)


if __name__ == '__main__':
	unittest.main()