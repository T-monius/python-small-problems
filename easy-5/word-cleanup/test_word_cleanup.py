import unittest
from word_cleanup import cleanup

class TestWordCleanup(unittest.TestCase):
    def test_rando_phrase(self):
        phrase = "---what's my +*& line?"
        desired_clean_str = ' what s my line '
        clean_str = cleanup(phrase)
        self.assertEqual(clean_str, desired_clean_str)


if __name__ == '__main__':
    unittest.main()