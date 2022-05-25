'''A module for testing the merge_sort module'''
import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    '''A class for testing the merge_sort module'''
    def test_simplest_list_of_numbers(self):
        '''Test a list containing just a single number'''
        nums = [1]
        sorted_nums = merge_sort(nums)
        self.assertEqual(sorted_nums, [1])

    def test_slightly_more_complex_list_of_numbers(self):
        '''Test a list of two numbers'''
        nums = [2, 1]
        sorted_nums = merge_sort(nums)
        self.assertEqual(sorted_nums, [1, 2])

    def test_another_short_list_of_numbers(self):
        '''Test another list of two numbers'''
        nums = [5, 3]
        sorted_nums = merge_sort(nums)
        self.assertEqual(sorted_nums, [3, 5])

    def test_another_list_of_numbers(self):
        '''Test a list of several numbers'''
        nums = [9, 5, 7, 1]
        sorted_nums = merge_sort(nums)
        self.assertEqual(sorted_nums, [1, 5, 7, 9])

    def test_a_long_list_of_numbers(self):
        '''Test a long list of numbers that is also of odd length'''
        nums = [
            7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46
        ]
        sorted_nums = merge_sort(nums)
        self.assertEqual(sorted_nums, [
            1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54
        ])

    def test_names(self):
        '''Test a list of names, or strings'''
        names = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
        sorted_names = merge_sort(names)
        self.assertEqual(sorted_names, [
            'Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler'
        ])


if __name__ == '__main__':
    unittest.main()
