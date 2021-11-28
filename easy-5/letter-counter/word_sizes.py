'''A module for determining sizes of words in strings'''

def word_sizes(phrase):
    '''Return a count of occurrences of lengths of words'''
    len_occurrences = {}
    if not phrase:
        return len_occurrences

    for word in phrase.split(' '):
        if len_occurrences.get(len(word)):
            len_occurrences[len(word)] += 1
            continue

        len_occurrences[len(word)] = 1

    return len_occurrences