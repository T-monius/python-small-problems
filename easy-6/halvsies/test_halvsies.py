'''A module for testing 'halsies' list splitting module'''
import unittest
from halvsies import slice_in_half

class TestHalvsies(unittest.TestCase):
    '''A class for testing splitting Lists'''
    def test_four_nums(self):
        '''Test a list of four numbers'''
        nums = [1, 2, 3, 4]
        slices = slice_in_half(nums)
        self.assertEqual(slices, [[1, 2], [3, 4]])

    def test_five_nums(self):
        '''Test a list of five numbers'''
        nums = [1, 5, 2, 4, 3]
        slices = slice_in_half(nums)
        self.assertEqual(slices, [[1, 5, 2], [4, 3]])

    def test_one_number_list(self):
        '''Test a list of a single digit'''
        nums = [5]
        slices = slice_in_half(nums)
        self.assertEqual(slices, [[5], []])

    def test_empty_list(self):
        '''Test an empty list'''
        nums = []
        slices = slice_in_half(nums)
        self.assertEqual(slices, [[], []])


if __name__ == '__main__':
    unittest.main()
