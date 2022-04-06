'''A module to test the tri_angles module'''
import unittest
from tri_angles import triangle

class TestTriAngles(unittest.TestCase):
    '''A class to test the tri_angles module'''
    def test_acute_triangle(self):
        '''Test that a triangle with all angles less than 90 is
           acute'''
        angle_zero = 60
        angle_one = 70
        angle_two = 50
        triangle_type = triangle(angle_zero, angle_one, angle_two)
        self.assertEqual(triangle_type, 'acute')

    def test_right_triangle(self):
        '''Test that a triangle with one angle less than 90 is
           right'''
        angle_zero = 30
        angle_one = 90
        angle_two = 60
        triangle_type = triangle(angle_zero, angle_one, angle_two)
        self.assertEqual(triangle_type, 'right')

    def test_obtuse_triangle(self):
        '''Test that a triangle with one angles greater than 90 is
           obtuse'''
        angle_zero = 120
        angle_one = 50
        angle_two = 10
        triangle_type = triangle(angle_zero, angle_one, angle_two)
        self.assertEqual(triangle_type, 'obtuse')

    def test_zero_angle_is_an_invalid_triangle(self):
        '''Test that a triangle with a zero angle is invalid'''
        angle_zero = 0
        angle_one = 90
        angle_two = 90
        triangle_type = triangle(angle_zero, angle_one, angle_two)
        self.assertEqual(triangle_type, 'invalid')

    def test_three_angles_sum_less_than_180_not_triangle(self):
        '''Test that a triangle with a three angles that do not sum to
           180 is invalid'''
        angle_zero = 50
        angle_one = 50
        angle_two = 50
        triangle_type = triangle(angle_zero, angle_one, angle_two)
        self.assertEqual(triangle_type, 'invalid')


if __name__ == '__main__':
    unittest.main()
