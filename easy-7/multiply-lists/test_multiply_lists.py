'''A module to test multiply_lists module'''
import unittest
from multiply_lists import multiply_lists

class TestMultiplyLists(unittest.TestCase):
    '''A class to test multiply_lists module'''
    def test_three_element_lists(self):
        '''Test two lists with three elements each'''
        primary = [3, 5, 7]
        secondary = [9, 10, 11]
        products = multiply_lists(primary, secondary)
        self.assertEqual(products, [27, 50, 77])


if __name__ == '__main__':
    unittest.main()
