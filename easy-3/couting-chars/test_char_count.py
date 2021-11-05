import unittest
from char_count import char_count

class TestCharCount(unittest.TestCase):
    def test_walk(self):
        phrase = 'walk'
        expected_count = 4
        actual_count = char_count(phrase)
        self.assertEqual(actual_count, expected_count)

    def test_three_word_phrase(self):
        phrase = "walk, don't run"
        expected_count = 13
        actual_count = char_count(phrase)
        self.assertEqual(actual_count, expected_count)

if __name__ == '__main__':
    unittest.main()