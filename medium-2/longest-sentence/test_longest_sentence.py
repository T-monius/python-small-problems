'''A module for testing the longest_sentence module'''
import unittest
from longest_sentence import read_file, longest_sentence_with_count

LONGEST_SENTENCE_FROM_FOUR_SCORE = ' It is rather for\n\
us to be here dedicated to the great task remaining\n\
before us -- that from these honored dead we take\n\
increased devotion to that cause for which they gave\n\
the last full measure of devotion -- that we here highly\n\
resolve that these dead shall not have died in vain\n\
-- that this nation, under God, shall have a new birth\n\
of freedom -- and that government of the people, by\n\
the people, for the people, shall not perish from the\n\
earth'

class TestLongestSentence(unittest.TestCase):
    '''A class for testing the longest_sentence module'''
    def test_reading_a_file(self):
        '''Test reading an example file'''
        filepath = 'example.txt'
        content = read_file(filepath)
        self.assertEqual(content, 'Hello world.')

    def test_four_score(self):
        '''Test a text of the emancipation proclamation address'''
        filepath = 'four_score.txt'
        sentence, count = longest_sentence_with_count(filepath)
        self.assertEqual(count, 86)
        self.assertEqual(sentence, LONGEST_SENTENCE_FROM_FOUR_SCORE)


if __name__ == '__main__':
    unittest.main()
