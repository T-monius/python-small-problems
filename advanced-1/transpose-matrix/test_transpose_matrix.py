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


if __name__ == '__main__':
    unittest.main()
