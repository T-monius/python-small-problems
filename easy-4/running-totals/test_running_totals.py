import unittest
from running_total import running_total

class TestRunningTotals(unittest.TestCase):
    def test_three_integers(self):
        numbers = [2, 5, 13]
        totals = running_total(numbers)
        self.assertEqual(totals, [2, 7, 20])

    def test_five_integers(self):
        numbers = [14, 11, 7, 15, 20]
        totals = running_total(numbers)
        self.assertEqual(totals, [14, 25, 32, 47, 67])

    def test_one_integer(self):
        numbers = [3]
        totals = running_total(numbers)
        self.assertEqual(totals, [3])

    def test_one_integer(self):
        numbers = []
        totals = running_total(numbers)
        self.assertEqual(totals, [])


if __name__ == '__main__':
    unittest.main()