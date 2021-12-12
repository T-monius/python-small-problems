'''A module for testing combining_two_lists'''
import unittest
from combining_two_lists import interleave

class TestCombiningTwoLists(unittest.TestCase):
    '''A class for testing combining_two_lists module'''
    def test_num_list_and_alpha_list(self):
        '''Test combining a list of numbers with one of alphas'''
        nums = [1, 2, 3]
        alphas = ['a', 'b', 'c']
        interleaved = interleave(nums, alphas)
        self.assertEqual(interleaved, [1, 'a', 2, 'b', 3, 'c'])

    def test_two_empty_lists(self):
        '''Test interleaving two empty lists'''
        empty_one = []
        empty_two = []
        interleaved = interleave(empty_one, empty_two)
        self.assertEqual(interleaved, [])


if __name__ == '__main__':
    unittest.main()
