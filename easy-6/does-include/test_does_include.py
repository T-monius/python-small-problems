'''A Class for testing whether a value is included in a list'''
import unittest
from does_include import does_include

class TestDoesInclude(unittest.TestCase):
    '''A Class for testing whether a value is included in a list'''
    def test_five_nums(self):
        '''Test a list of five nums containing search value'''
        nums = [1, 2, 3, 4, 5]
        search_val = 3
        is_present = does_include(nums, search_val)
        self.assertTrue(is_present)

    def test_five_nums_num_not_present(self):
        '''Test a list of five nums not containing search value'''
        nums = [1, 2, 3, 4, 5]
        search_val = 6
        is_present = does_include(nums, search_val)
        self.assertFalse(is_present)

    def test_empty_list(self):
        '''Test an empty list'''
        lst = []
        search_val = 3
        is_present = does_include(lst, search_val)
        self.assertFalse(is_present)

    def test_none_values(self):
        '''Test a list of None values'''
        lst = [None]
        search_val = None
        is_present = does_include(lst, search_val)
        self.assertTrue(is_present)

    def test_empty_list_verse_none(self):
        '''Test an empty list for a None value'''
        lst = []
        search_val = None
        is_present = does_include(lst, search_val)
        self.assertFalse(is_present)


if __name__ == '__main__':
    unittest.main()
