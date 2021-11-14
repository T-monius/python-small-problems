# test_what_century.py
import unittest
from what_century import century_count, what_century, get_suffix

class TestWhatCentury(unittest.TestCase):
    def test_century_count_two_thousand(self):
        numeric_year = 2000
        result = century_count(numeric_year)
        self.assertEqual(result, 20)

    def test_century_count_two_thousand_and_one(self):
        numeric_year = 2001
        result = century_count(numeric_year)
        self.assertEqual(result, 21)

    def test_century_count_nineteen_sixty_five(self):
        numeric_year = 1965
        result = century_count(numeric_year)
        self.assertEqual(result, 20)

    def test_century_count_three(self):
        numeric_year = 256
        result = century_count(numeric_year)
        self.assertEqual(result, 3)

    def test_century_count_five(self):
        numeric_year = 5
        result = century_count(numeric_year)
        self.assertEqual(result, 1)

    def test_century_count_ten_thousand_one_zero_three(self):
        numeric_year = 10103
        result = century_count(numeric_year)
        self.assertEqual(result, 102)

    def test_century_count_thousand_fifty_two(self):
        numeric_year = 1052
        result = century_count(numeric_year)
        self.assertEqual(result, 11)

    def test_century_count_eleven_twenty_seven(self):
        numeric_year = 1127
        result = century_count(numeric_year)
        self.assertEqual(result, 12)

    def test_century_count_eleven_two_hundred_one(self):
        numeric_year = 11201
        result = century_count(numeric_year)
        self.assertEqual(result, 113)

    def test_what_century_two_thousand(self):
        numeric_year = 2000
        result = what_century(numeric_year)
        self.assertEqual(result, '20th')

    def test_what_century_two_thousand_and_one(self):
        numeric_year = 2001
        result = what_century(numeric_year)
        self.assertEqual(result, '21st')

    def test_what_century_nineteen_sixty_five(self):
        numeric_year = 1965
        result = what_century(numeric_year)
        self.assertEqual(result, '20th')

    def test_what_century_three(self):
        numeric_year = 256
        result = what_century(numeric_year)
        self.assertEqual(result, '3rd')

    def test_what_century_five(self):
        numeric_year = 5
        result = what_century(numeric_year)
        self.assertEqual(result, '1st')

    def test_what_century_ten_thousand_one_zero_three(self):
        numeric_year = 10103
        result = what_century(numeric_year)
        self.assertEqual(result, '102nd')

    def test_what_century_thousand_fifty_two(self):
        numeric_year = 1052
        result = what_century(numeric_year)
        self.assertEqual(result, '11th')

    def test_what_century_eleven_twenty_seven(self):
        numeric_year = 1127
        result = what_century(numeric_year)
        self.assertEqual(result, '12th')

    def test_what_century_eleven_two_hundred_one(self):
        numeric_year = 11201
        result = what_century(numeric_year)
        self.assertEqual(result, '113th')


if __name__ == '__main__':
    unittest.main()
