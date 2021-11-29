'''A module for determining sizes of words in strings'''

def cleanup(phrase):
    '''Remove non-alpha chararters from a word'''
    only_alphas = ''

    for char in phrase:
        if char.isalpha():
            only_alphas += char

    return only_alphas


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


def exact_word_sizes(phrase):
    '''Return a count of occurrences of word lengths by alphas'''
    len_occurrences = {}
    if not phrase:
        return len_occurrences

    clean_words = [cleanup(word) for word in phrase.split(' ')]

    for word in clean_words:
        if len_occurrences.get(len(word)):
            len_occurrences[len(word)] += 1
            continue

        len_occurrences[len(word)] = 1

    return len_occurrences
