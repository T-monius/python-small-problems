''' A module for testing the merge_sorted_lists module'''
import unittest
from merge_sorted_lists import merge

class TestMergeSortedLists(unittest.TestCase):
    '''A class for testing the mege_sorted_lists module'''
    def test_two_lists_of_three_integer_elements(self):
        '''Test mergring two lists of three integer elements into a
           single list without mutating the inputs'''
        ints = [1, 5, 9]
        ints1 = [2, 6, 8]
        merged = merge(ints, ints1)
        self.assertEqual(merged, [1, 2, 5, 6, 8, 9])
        self.assertEqual(ints, [1, 5, 9])
        self.assertEqual(ints1, [2, 6, 8])

    def test_uneven_length_lists(self):
        '''Test mergring two lists of different lengths into a single
           list without mutating the inputs'''
        ints = [1, 1, 3]
        ints1 = [2, 2]
        merged = merge(ints, ints1)
        self.assertEqual(merged, [1, 1, 2, 2, 3])
        self.assertEqual(ints, [1, 1, 3])
        self.assertEqual(ints1, [2, 2])

    def test_lists_where_one_is_empty(self):
        '''Test mergring two lists where one is empty list without
           mutating the inputs'''
        ints = []
        ints1 = [1, 4, 5]
        merged = merge(ints, ints1)
        self.assertEqual(merged, [1, 4, 5])
        self.assertEqual(ints, [])
        self.assertEqual(ints1, [1, 4, 5])

    def test_lists_where_other_one_is_empty(self):
        '''Test mergring two lists where one is empty list without
           mutating the inputs'''
        ints = [1, 4, 5]
        ints1 = []
        merged = merge(ints, ints1)
        self.assertEqual(merged, [1, 4, 5])
        self.assertEqual(ints, [1, 4, 5])
        self.assertEqual(ints1, [])


if __name__ == '__main__':
    unittest.main()
