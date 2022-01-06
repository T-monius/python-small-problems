'''A module for testing all_substrings module'''
import unittest
from all_substrings import substrings

class TestAllSubstrings(unittest.TestCase):
    '''A class for testing all_substrings module'''
    def test_abcs_upto_e(self):
        '''Retrieve all substrings in list from of the alphabet up
           to the letter e'''
        abcs = 'abcde'
        all_substrings_ordered = substrings(abcs)
        self.assertEqual(all_substrings_ordered, [
              'a', 'ab', 'abc', 'abcd', 'abcde',
              'b', 'bc', 'bcd', 'bcde',
              'c', 'cd', 'cde',
              'd', 'de',
              'e'
            ])


if __name__ == '__main__':
    unittest.main()
