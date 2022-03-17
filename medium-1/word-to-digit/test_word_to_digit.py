'''A module for testing the word_to_digit module'''
import unittest
from word_to_digit import word_to_digit, convert_a_word_to_digit

class TestWordToDigit(unittest.TestCase):
    '''A class for testing the word_to_digit module'''
    def test_convert_a_word_to_digit_without_punctuation(self):
        '''Test a word that has no punctuation'''
        word = 'the'
        result = convert_a_word_to_digit(word)
        self.assertEqual(result, word)

    def test_convert_a_word_to_digit_with_punctuation(self):
        '''Test a word that has punctuation'''
        word = 'the.'
        result = convert_a_word_to_digit(word)
        self.assertEqual(result, word)

    def test_convert_a_word_to_digit_with_varied_punctuation(self):
        '''Test a word that has punctuation'''
        word = 'the!'
        result = convert_a_word_to_digit(word)
        self.assertEqual(result, word)

    def test_convert_a_word_to_digit_with_number(self):
        '''Test a word that represents a number'''
        word = 'four'
        result = convert_a_word_to_digit(word)
        self.assertEqual(result, '4')

    def test_convert_a_word_to_digit_with_number_and_punctuation(self):
        '''Test a word that has punctuation and represents a number'''
        word = 'four.'
        result = convert_a_word_to_digit(word)
        self.assertEqual(result, '4.')

    def test_a_sentence_with_spelled_out_numbers(self):
        '''Test a sentence of words some being spelled out numbers as
           well as punctuation'''
        sentence = 'Please call me at five five five one two three four.' \
                   ' Thanks.'
        new_sentence = word_to_digit(sentence)
        self.assertEqual(
            new_sentence,
            'Please call me at 5 5 5 1 2 3 4. Thanks.'
        )


if __name__ == '__main__':
    unittest.main()
