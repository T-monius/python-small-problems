import unittest
from leap_years import is_leap_year

class TestLeapYears(unittest.TestCase):
    def test_twenty_sixteen(self):
        year = 2016
        result = is_leap_year(year)
        self.assertTrue(result)

    def test_twenty_four_hundred(self):
        year = 2400
        result = is_leap_year(year)
        self.assertTrue(result)

    def test_two_hundred_forty_thousand(self):
        year = 240000
        result = is_leap_year(year)
        self.assertTrue(result)

    def test_two_thousand(self):
        year = 2000
        result = is_leap_year(year)
        self.assertTrue(result)

    def test_seventeen_fifty_two(self):
        year = 1752
        result = is_leap_year(year)
        self.assertTrue(result)

    def test_four_hundred(self):
        year = 400
        result = is_leap_year(year)
        self.assertTrue(result)

    def test_twenty_fifteen(self):
        year = 2015
        result = is_leap_year(year)
        self.assertFalse(result)

    def test_twenty_one_hundred(self):
        year = 2100
        result = is_leap_year(year)
        self.assertFalse(result)

    def test_two_hundred_forty_thousand_and_one(self):
        year = 240001
        result = is_leap_year(year)
        self.assertFalse(result)

    def test_nineteen_hundred(self):
        year = 1900
        result = is_leap_year(year)
        self.assertFalse(result)

    def test_seventeen_hundred(self):
        year = 1700
        result = is_leap_year(year)
        self.assertTrue(result)

    def test_one(self):
        year = 1
        result = is_leap_year(year)
        self.assertFalse(result)

    def test_one_hundred(self):
        year = 100
        result = is_leap_year(year)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
