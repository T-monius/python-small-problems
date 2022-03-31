'''A module for verifying correctness of parentheses in text'''

OPENING_PARENTHESIS = '('
CLOSING_PARENTHESIS = ')'

def instantiate_counts_for_chars(chars):
    '''Return a dictionary of counts for each char in input list'''
    counts = {}

    for char in chars:
        counts[char] = 0

    return counts


def is_balanced(text):
    '''Return a boolean indicating if the parentheses in text occur in
       an idiomatic manner'''
    offset_chars = [OPENING_PARENTHESIS, CLOSING_PARENTHESIS]
    counts = instantiate_counts_for_chars(offset_chars)
    for char in text:
        if counts[CLOSING_PARENTHESIS] > counts[OPENING_PARENTHESIS]:
            return False
        if char in offset_chars:
            counts[char] += 1

    return counts[OPENING_PARENTHESIS] == counts[CLOSING_PARENTHESIS]
