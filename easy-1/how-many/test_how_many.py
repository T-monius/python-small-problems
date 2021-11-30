import unittest
from how_many import counts

class TestHowMany(unittest.TestCase):
	def test_vehicles(self):
		vehicles = [
		    'car', 'car', 'truck', 'car', 'SUV', 'truck',
		    'motorcycle', 'motorcycle', 'car', 'truck'
		]
		expected_counts = {
			'car': 4,
			'truck': 3,
			'SUV': 1,
			'motorcycle': 2
		}
		resuolt = counts(vehicles)
		self.assertEqual(resuolt, expected_counts)

if __name__ == '__main__':
	unittest.main()