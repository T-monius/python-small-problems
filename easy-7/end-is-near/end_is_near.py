'''A module for working with words found in strings'''

def penultimate(phrase):
    '''Return the penultimate word in a string input where there are
       at least two words present'''
    words = phrase.split()
    word_slice = words[-2:-1]
    penultimate_word = word_slice.pop()

    return penultimate_word
