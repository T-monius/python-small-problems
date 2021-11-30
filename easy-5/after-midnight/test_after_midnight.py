'''A module for testing after_midnight module'''
import unittest
from after_midnight import time_of_day

class TestTimeOfDay(unittest.TestCase):
    '''Test time_of_day funtion'''
    def test_zero(self):
        '''Test time_of_day function with input of zero'''
        minute_time = 0
        twenty_four_hr_time = time_of_day(minute_time)
        self.assertEqual(twenty_four_hr_time, '00:00')

    def test_negative_three(self):
        '''Test time_of_day function with input of negative 3'''
        minute_time = -3
        twenty_four_hr_time = time_of_day(minute_time)
        self.assertEqual(twenty_four_hr_time, '23:57')

    def test_thirty_five(self):
        '''Test time_of_day function with input of 35'''
        minute_time = 35
        twenty_four_hr_time = time_of_day(minute_time)
        self.assertEqual(twenty_four_hr_time, '00:35')

    def test_negative_fourteen_thiry_seven(self):
        '''Test time_of_day function with input of -1437'''
        minute_time = -1437
        twenty_four_hr_time = time_of_day(minute_time)
        self.assertEqual(twenty_four_hr_time, '00:03')

    def test_three_thousand(self):
        '''Test time_of_day function with input of 3000'''
        minute_time = 3000
        twenty_four_hr_time = time_of_day(minute_time)
        self.assertEqual(twenty_four_hr_time, '02:00')

    def test_eight_hundred(self):
        '''Test time_of_day function with input of 800'''
        minute_time = 800
        twenty_four_hr_time = time_of_day(minute_time)
        self.assertEqual(twenty_four_hr_time, '13:20')

    def test_negative_fourty_two_thirty_one(self):
        '''Test time_of_day function with input of zero'''
        minute_time = -4231
        twenty_four_hr_time = time_of_day(minute_time)
        self.assertEqual(twenty_four_hr_time, '01:29')


if __name__ == '__main__':
    unittest.main()
