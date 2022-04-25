'''A module for testing the transpose_matrix module'''
import unittest
from transpose_matrix import transpose

class TestTransposeMatrix(unittest.TestCase):
    '''A class for testing the transpose_matrix module'''
    def test_three_by_three(self):
        '''Test transposing a 3x3 matrix'''
        matrix = [[1, 5, 8], [4, 7, 2], [3, 9, 6]]
        new_matrix = transpose(matrix)
        self.assertEqual(new_matrix, [[1, 4, 3], [5, 7, 9], [8, 2, 6]])
        # Does not mutate
        self.assertEqual(matrix, [[1, 5, 8], [4, 7, 2], [3, 9, 6]])

    def test_four_by_one(self):
        '''Test transposing a 4x1 matrix'''
        matrix = [
            [1, 2, 3, 4],
        ]
        new_matrix = transpose(matrix)
        self.assertEqual(new_matrix, [
            [1],
            [2],
            [3],
            [4],
        ])
        # Does not mutate
        self.assertEqual(matrix, [
            [1, 2, 3, 4]
        ])

    def test_one_by_four(self):
        '''Test transposing a 1x4 matrix'''
        matrix = [
            [1],
            [2],
            [3],
            [4],
        ]
        new_matrix = transpose(matrix)
        self.assertEqual(new_matrix, [
            [1, 2, 3, 4],
        ])
        # Does not mutate
        self.assertEqual(matrix, [
            [1],
            [2],
            [3],
            [4],
        ])

    def test_five_by_three(self):
        '''Test transposing a 5x3 matrix'''
        matrix = [
            [1, 2, 3, 4, 5],
            [4, 3, 2, 1, 0],
            [3, 7, 8, 6, 2],
        ]
        new_matrix = transpose(matrix)
        self.assertEqual(new_matrix, [
            [1, 4, 3],
            [2, 3, 7],
            [3, 2, 8],
            [4, 1, 6],
            [5, 0, 2],
        ])
        # Does not mutate
        self.assertEqual(matrix, [
            [1, 2, 3, 4, 5],
            [4, 3, 2, 1, 0],
            [3, 7, 8, 6, 2],
        ])

    def test_one_by_one(self):
        '''Test transposing a 1x1 matrix'''
        matrix = [
            [1],
        ]
        new_matrix = transpose(matrix)
        self.assertEqual(new_matrix, [
            [1],
        ])
        # Does not mutate
        self.assertEqual(matrix, [
            [1],
        ])


if __name__ == '__main__':
    unittest.main()
