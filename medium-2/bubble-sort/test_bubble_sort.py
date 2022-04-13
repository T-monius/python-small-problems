'''A module for testing the bubble_sort module'''
import unittest
from bubble_sort import sort_the_bubble_way_in_place

class TestBubbleSort(unittest.TestCase):
    '''A class for testing the bubble_sort module'''
    def test_a_two_element_list(self):
        '''Test a list of just two integers'''
        two_nums = [5, 3]
        sorted_nums = sort_the_bubble_way_in_place(two_nums)
        self.assertEqual(sorted_nums, [3, 5])


    def test_a_multiple_element_list(self):
        '''Test a list of multiple elements'''
        nums = [2, 6, 1, 4, 7]
        sorted_nums = sort_the_bubble_way_in_place(nums)
        self.assertEqual(sorted_nums, [1, 2, 4, 6, 7])


    def test_a_list_of_names(self):
        '''Test a list of names'''
        names = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
        sorted_nums = sort_the_bubble_way_in_place(names)
        self.assertEqual(sorted_nums, ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler'])


if __name__ == '__main__':
    unittest.main()
