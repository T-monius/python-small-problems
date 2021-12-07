'''A module for testing cute_angle module that works with degrees,
   minutes, and seconds'''
import unittest
from cute_angles import dms

class TestDMS(unittest.TestCase):
    '''A class for testing `dms` function for angle conversion'''
    def test_thirty(self):
        '''Test converting int 30 to degrees, minutes, seconds'''
        angle = 30
        str_angle = dms(angle)
        self.assertEqual(str_angle, "30°00'00\"")

    def test_seventy_six_point_seventy_three(self):
        '''Test converting int 76.73 to degrees, minutes, seconds'''
        angle = 76.73
        str_angle = dms(angle)
        self.assertEqual(str_angle, "76°43'48\"")

    def test_two_fifty_four_point_6(self):
        '''Test converting int 254.6 to degrees, minutes, seconds'''
        angle = 254.6
        str_angle = dms(angle)
        self.assertEqual(str_angle, "254°36'00\"")

    def test_ninety_three_point_blah_blah(self):
        '''Test converting int 93.034773 to degrees, minutes, seconds'''
        angle = 93.034773
        str_angle = dms(angle)
        self.assertEqual(str_angle, "93°02'05\"")

    def test_zero(self):
        '''Test converting int 0 to degrees, minutes, seconds'''
        angle = 0
        str_angle = dms(angle)
        self.assertEqual(str_angle, "0°00'00\"")

    def test_three_sixty(self):
        '''Test converting int 360 to degrees, minutes, seconds'''
        angle = 360
        str_angle = dms(angle)
        self.assertEqual(str_angle, "360°00'00\"")


if __name__ == '__main__':
    unittest.main()
