'''A module for testing letter_case_count module'''
import unittest
from letter_case_count import letter_case_count

class TestLetterCaseCount(unittest.TestCase):
    '''A class for testing letter_case_count module'''
    def test_alphanumeric(self):
        '''Test a string with alphanumeric and space characters'''
        alphanum = 'abCdef 123'
        case_count = letter_case_count(alphanum)
        self.assertEqual(
            case_count,
            { 'lowercase': 5, 'uppercase': 1, 'neither': 4 }
        )

    def test_alpha_and_specia_chars(self):
        '''Test a string with alpha and special characters'''
        mixed_chars = 'AbCd +Ef'
        case_count = letter_case_count(mixed_chars)
        self.assertEqual(
            case_count,
            { 'lowercase': 3, 'uppercase': 3, 'neither': 2 }
        )

    def test_nums(self):
        '''Test a string of all numebrs'''
        nums = '123'
        case_count = letter_case_count(nums)
        self.assertEqual(
            case_count,
            { 'lowercase': 0, 'uppercase': 0, 'neither': 3 }
        )

    def test_empty_string(self):
        '''Test an empty string'''
        empty_str = ''
        case_count = letter_case_count(empty_str)
        self.assertEqual(
            case_count,
            { 'lowercase': 0, 'uppercase': 0, 'neither': 0 }
        )


if __name__ == '__main__':
    unittest.main()
