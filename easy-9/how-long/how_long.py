'''A module for deriving lengths of words in source strings'''

def word_lengths(src):
    '''Return a list of words from an input string where words are non-
       whitespace substrings that are space separated'''
    words = src.split()
    lengths = [f'{word} {len(word)}' for word in words]

    return lengths
