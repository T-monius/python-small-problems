import unittest
from word_sizes import word_sizes, exact_word_sizes

class TestWordSizes(unittest.TestCase):
    def test_short_phrase(self):
        phrase = 'Four score and seven.'
        len_occurrences = word_sizes(phrase)
        self.assertEqual(len_occurrences, { 3: 1, 4: 1, 5: 1, 6: 1 })

    def test_long_phrase(self):
        phrase = 'Hey diddle diddle, the cat and the fiddle!'
        len_occurrences = word_sizes(phrase)
        self.assertEqual(len_occurrences, { 3: 5, 6: 1, 7: 2 })

    def test_catch_phrase(self):
        phrase = "What's up doc?"
        len_occurrences = word_sizes(phrase)
        self.assertEqual(len_occurrences, { 6: 1, 2: 1, 4: 1 })

    def test_empty_str(self):
        phrase = ''
        len_occurrences = word_sizes(phrase)
        self.assertEqual(len_occurrences, {})

    def test_declaration(self):
        phrase = 'Four score and seven.'
        len_occurrences = exact_word_sizes(phrase)
        self.assertEqual(len_occurrences, { 3: 1, 4: 1, 5: 2 })

    def test_another_empty_str(self):
        phrase = ''
        len_occurrences = exact_word_sizes(phrase)
        self.assertEqual(len_occurrences, {})

    def test_riddle(self):
        riddle = 'Hey diddle diddle, the cat and the fiddle!'
        len_occurrences = exact_word_sizes(riddle)
        self.assertEqual(len_occurrences, { 3: 5, 6: 3 })

    def test_catch_phrase_again(self):
        catch_phrase = "What's up doc?"
        len_occurrences = exact_word_sizes(catch_phrase)
        self.assertEqual(len_occurrences, { 5: 1, 2: 1, 3: 1 })


if __name__ == '__main__':
    unittest.main()