'''A module for testing the multiply_pairs module'''
import unittest
from multiply_pairs import multiply_all_pairs

class TestMultiplyPairs(unittest.TestCase):
    '''A class for testing the multiply_pairs module'''
    def test_two_value_list_by_three_value_list(self):
        '''Multiply all values of a two element list by all values of
           a three element list'''
        primary = [2, 4]
        secondary = [4, 3, 1, 2]
        ordered_products = multiply_all_pairs(primary, secondary)
        self.assertEqual(ordered_products, [2, 4, 4, 6, 8, 8, 12, 16])


if __name__ == '__main__':
    unittest.main()
