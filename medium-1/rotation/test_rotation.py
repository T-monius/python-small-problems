'''A module for testing the rotation module'''
import unittest
from rotation import rotate_list, rotate_rightmost_digits

class TestRotation(unittest.TestCase):
    '''A class for testing the rotation module'''
    def test_rotate_list_with_numbers(self):
        '''Test an all number input to rotate_list'''
        numbers = [7, 3, 5, 2, 9, 1]
        rotated = rotate_list(numbers)
        self.assertEqual(rotated, [3, 5, 2, 9, 1, 7])

    def test_rotate_list_with_letters(self):
        letters = ['a', 'b', 'c']
        rotated = rotate_list(letters)
        self.assertEqual(rotated, ['b', 'c', 'a'])

    def test_rotate_list_with_a_single_letter(self):
        letter = ['a']
        rotated = rotate_list(letter)
        self.assertEqual(rotated, ['a'])

    def test_rotate_list_does_not_mutate_input_list(self):
        x = [1, 2, 3, 4]
        rotate_list(x)
        self.assertEqual(x, [1, 2, 3, 4])

    def test_rotate_rightmost_digits_one(self):
        n = 1
        num = 735291
        rotated_right = rotate_rightmost_digits(num, n)
        self.assertEqual(rotated_right, 735291)

    def test_rotate_rightmost_digits_two(self):
        n = 2
        num = 735291
        rotated_right = rotate_rightmost_digits(num, n)
        self.assertEqual(rotated_right, 735219)

    def test_rotate_rightmost_digits_three(self):
        n = 3
        num = 735291
        rotated_right = rotate_rightmost_digits(num, n)
        self.assertEqual(rotated_right, 735912)

    def test_rotate_rightmost_digits_four(self):
        n = 4
        num = 735291
        rotated_right = rotate_rightmost_digits(num, n)
        self.assertEqual(rotated_right, 732915)

    def test_rotate_rightmost_digits_five(self):
        n = 5
        num = 735291
        rotated_right = rotate_rightmost_digits(num, n)
        self.assertEqual(rotated_right, 752913)

    def test_rotate_rightmost_digits_six(self):
        n = 6
        num = 735291
        rotated_right = rotate_rightmost_digits(num, n)
        self.assertEqual(rotated_right, 352917)


if __name__ == '__main__':
    unittest.main()
