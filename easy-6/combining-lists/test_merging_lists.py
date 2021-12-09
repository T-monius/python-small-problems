'''A module for testing the merging of two lists'''
import unittest

from merging_lists import uniq_combine

class TestMergingLists(unittest.TestCase):
    '''A class for testing merging of two lists w/o duplicates'''
    def test_all_nums_same_length(self):
        '''Merge two lists of numbers that are the same length'''
        nums1 = [1, 3, 5]
        nums2 = [3, 6, 9]
        combined = uniq_combine(nums1, nums2)
        self.assertEqual(combined, [1, 3, 5, 6, 9])

    def test_all_nums_different_lengths(self):
        '''Merge two lists of numbers of different lengths'''
        nums1 = [1, 3, 5]
        nums2 = [3, 6, 9, 11]
        combined = uniq_combine(nums1, nums2)
        self.assertEqual(combined, [1, 3, 5, 6, 9, 11])

    def test_alphas_same_length(self):
        '''Merge two lists of alphas of the same length'''
        alphas1 = ['a', 'b', 'c']
        alphas2 = ['b', 'd', 'f']
        combined = uniq_combine(alphas1, alphas2)
        self.assertEqual(combined, ['a', 'b', 'c', 'd','f'])

    def test_alphas_differeing_length(self):
        '''Merge two lists of alphas of different lengths'''
        alphas1 = ['a', 'b', 'c', 'd']
        alphas2 = ['b', 'd', 'f']
        combined = uniq_combine(alphas1, alphas2)
        self.assertEqual(combined, ['a', 'b', 'c', 'd','f'])


if __name__ == '__main__':
    unittest.main()
