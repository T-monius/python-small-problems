'''A module to test the triangle_sides module'''
import unittest
from triangle_sides import triangle, is_valid_triangle

class TestTriangleSides(unittest.TestCase):
    '''A class to test the triangle_sides module'''
    def test_a_trianlge_of_three_equal_non_zero_sides(self):
        '''Test a triangle with a side three non-zero sides as valid'''
        side_zero = 3
        side_one = 3
        side_two = 3
        sides_sorted = [side_zero, side_one, side_two]
        validity = is_valid_triangle(sides_sorted)
        self.assertTrue(validity)

    def test_invalid_for_zero_length_side_as_false(self):
        '''Test a triangle with a side that is zero, invalid'''
        side_zero = 0
        side_one = 3
        side_two = 3
        sides_sorted = [side_zero, side_one, side_two]
        validity = is_valid_triangle(sides_sorted)
        self.assertFalse(validity)

    def test_another_invalid_for_zero_length_side_as_false(self):
        '''Test a triangle with a side that is zero, invalid'''
        side_zero = 3
        side_one = 0
        side_two = 3
        sides_sorted = [side_one, side_zero, side_two]
        validity = is_valid_triangle(sides_sorted)
        self.assertFalse(validity)

    def test_validity_false_for_two_sides_not_greater_than_third(self):
        '''Test a triangle with two shorter sided not greater than the
           the longest to return False'''
        side_zero = 3
        side_one = 1
        side_two = 1
        sides = [side_zero, side_one, side_two]
        sides.sort()
        validity = is_valid_triangle(sides)
        self.assertFalse(validity)

    def test_almost_isosceles(self):
        '''Test a triangle with two equal sides, isosceles'''
        side_zero = 1.5
        side_one = 3
        side_two = 1.5
        sides = [side_zero, side_one, side_two]
        sides.sort()
        triangle_type = is_valid_triangle(sides)
        self.assertFalse(triangle_type)

    def test_equilateral(self):
        '''Test a triangle with three equal sides, equilateral'''
        side_zero = 3
        side_one = 3
        side_two = 3
        triangle_type = triangle(side_zero, side_one, side_two)
        self.assertEqual(triangle_type, 'equilateral')


    def test_isosceles(self):
        '''Test a triangle with two equal sides, isosceles'''
        side_zero = 3
        side_one = 3
        side_two = 1.5
        triangle_type = triangle(side_zero, side_one, side_two)
        self.assertEqual(triangle_type, 'isosceles')

    def test_another_isosceles(self):
        '''Test a triangle with two equal sides, isosceles'''
        side_zero = 2
        side_one = 1.5
        side_two = 1.5
        triangle_type = triangle(side_zero, side_one, side_two)
        self.assertEqual(triangle_type, 'isosceles')

    def test_scalene(self):
        '''Test a triangle with unequal sides, scalene'''
        side_zero = 3
        side_one = 4
        side_two = 5
        triangle_type = triangle(side_zero, side_one, side_two)
        self.assertEqual(triangle_type, 'scalene')

    def test_invalid_for_zero_length_side(self):
        '''Test a triangle with a side that is zero, invalid'''
        side_zero = 0
        side_one = 3
        side_two = 3
        triangle_type = triangle(side_zero, side_one, side_two)
        self.assertEqual(triangle_type, 'invalid')

    def test_invalid_for_another_zero_length_side(self):
        '''Test a triangle with a side that is zero, invalid'''
        side_zero = 3
        side_one = 0
        side_two = 3
        triangle_type = triangle(side_zero, side_one, side_two)
        self.assertEqual(triangle_type, 'invalid')

    def test_another_invalid(self):
        '''Test a triangle with two shortest sides that don't add to a
           greater length than the longest, invalid'''
        side_zero = 3
        side_one = 1
        side_two = 1
        triangle_type = triangle(side_zero, side_one, side_two)
        self.assertEqual(triangle_type, 'invalid')


if __name__ == '__main__':
    unittest.main()
