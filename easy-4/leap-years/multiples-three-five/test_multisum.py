import unittest
from multisum import multisum

class TestMultiSum(unittest.TestCase):
    def test_three(self):
        range_limit = 3
        result = multisum(range_limit)
        self.assertEqual(result, 3)

    def test_five(self):
        range_limit = 5
        result = multisum(range_limit)
        self.assertEqual(result, 8)

    def test_ten(self):
        range_limit = 10
        result = multisum(range_limit)
        self.assertEqual(result, 33)

    def test_one_thousand(self):
        range_limit = 1000
        result = multisum(range_limit)
        self.assertEqual(result, 234168)


if __name__ == '__main__':
    unittest.main()