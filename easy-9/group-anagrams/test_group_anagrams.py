'''A module for testing the group_anagrams moduls'''
import unittest
from group_anagrams import grouped_anagrams

class TestGroupAnagrams(unittest.TestCase):
    '''A class for testing the group_anagrams module for finding
       anagrams in a list of words'''
    def test_list_of_four_letter_words(self):
        '''Find the anaagrams in a list of words that are all four
           letters'''
        four_letter_words = [
            'demo', 'none', 'tied', 'evil', 'dome', 'mode', 'live',
            'fowl', 'veil', 'wolf', 'diet', 'vile', 'edit', 'tide',
            'flow', 'neon'
        ]
        all_anagrams = grouped_anagrams(four_letter_words)
        self.assertEqual(all_anagrams, [
            ['dome', 'mode', 'demo'],
            ['neon', 'none'],
            ['diet', 'edit', 'tide', 'tied'],
            ['live', 'veil', 'vile', 'evil'],
            ['wolf', 'flow', 'fowl']
        ])


if __name__ == '__main__':
    unittest.main()
