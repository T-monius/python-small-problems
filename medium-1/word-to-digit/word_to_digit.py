'''A module for replacing word representations of certain numbers in
   text to digit representations'''

WORD_DIGIT_DICT = { 'zero': '0', 'one': '1', 'two': '2', 'three': '3',
                    'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                    'eight': '8', 'nine': '9' }

def convert_a_word_to_digit(word):
    '''Conditionally convert a word from a representation of a number
       to a numeric counterpart accounting for punctuation, or simply
       return words that aren't number related'''
    punctuation = '' if word[-1].isalnum() else word[-1]
    word = word[:-1] if punctuation else word
    word = WORD_DIGIT_DICT[word] if WORD_DIGIT_DICT.get(word) else word

    return word + punctuation



def word_to_digit(sentence):
    '''Replace occurrences of words representing certain numbers into
       their digit counterpart'''
    new_words = [convert_a_word_to_digit(word) for word in sentence.split()]

    return ' '.join(new_words)
