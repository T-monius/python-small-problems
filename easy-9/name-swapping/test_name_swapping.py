'''A module for testing the name_swapping module'''
import unittest
from name_swapping import swap_name

class TestNameSwapping(unittest.TestCase):
    '''A class for testing the name_swapping module'''
    def test_simple_name(self):
        '''Test a space separated common name'''
        name = 'Joe Roberts'
        swapped = swap_name(name)
        self.assertEqual(swapped, 'Roberts, Joe')


if __name__ == '__main__':
    unittest.main()
