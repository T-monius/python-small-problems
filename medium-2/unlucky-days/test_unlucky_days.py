'''A module to test the unlucky_days module that works with Friday the
   13ths'''
import unittest
from unlucky_days import friday_13th_count

class TestUnluckyDays(unittest.TestCase):
    '''A class to test the unlucky_days module that works with Friday
       the 13ths'''
    def test_twenty_fifteen(self):
        '''Determine how many Friday the thirteents are in the year
           2015'''
        year = 2015
        count = friday_13th_count(year)
        self.assertEqual(count, 3)

    def test_nineteen_eighty_six(self):
        '''Determine how many Friday the thirteents are in the year
           1986'''
        year = 1986
        count = friday_13th_count(year)
        self.assertEqual(count, 1)

    def test_twenty_nineteen(self):
        '''Determine how many Friday the thirteents are in the year
           2019'''
        year = 2019
        count = friday_13th_count(year)
        self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()
