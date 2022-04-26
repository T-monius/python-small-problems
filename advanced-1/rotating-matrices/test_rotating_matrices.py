'''A module for testing the rotate_matrices module'''
import unittest
from rotating_matrices import rotate90

class TestRotateMatrices(unittest.TestCase):
    '''A class for testing the rotate_matrices module'''
    def test_three_by_three(self):
        '''Rotate a 3x3 matrix'''
        matrix = [
          [1, 5, 8],
          [4, 7, 2],
          [3, 9, 6],
        ]
        rotated_matrix = rotate90(matrix)
        self.assertEqual(rotated_matrix, [
            [3, 4, 1],
            [9, 7, 5],
            [6, 2, 8],
        ])


    def test_four_by_two(self):
        '''Rotate a 4x2 matrix'''
        matrix = [
            [3, 7, 4, 2],
            [5, 1, 0, 8],
        ]
        rotated_matrix = rotate90(matrix)
        self.assertEqual(rotated_matrix, [
            [5, 3],
            [1, 7],
            [0, 4],
            [8, 2],
        ])


if __name__ == '__main__':
    unittest.main()
