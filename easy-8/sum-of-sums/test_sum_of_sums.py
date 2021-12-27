'''A module for testing sum_of_sums module'''
import unittest
from sum_of_sums import sum_of_sums

class TestSumOfSums(unittest.TestCase):
    '''A class for testing sum_of_sums module'''
    def test_three_element_list(self):
        '''Test a list of three numbers'''
        nums = [3, 5, 2]
        overall_sum = sum_of_sums(nums)
        self.assertEqual(overall_sum, 21)

    def test_four_element_list(self):
        '''Test a list of four numbers'''
        nums = [1, 5, 7, 3]
        overall_sum = sum_of_sums(nums)
        self.assertEqual(overall_sum, 36)

    def test_single_element_list(self):
        '''Test a list of one number'''
        nums = [4]
        overall_sum = sum_of_sums(nums)
        self.assertEqual(overall_sum, 4)

    def test_five_element_list(self):
        '''Test a list of five numbers'''
        nums = [1, 2, 3, 4, 5]
        overall_sum = sum_of_sums(nums)
        self.assertEqual(overall_sum, 35)


if __name__ == '__main__':
    unittest.main()
