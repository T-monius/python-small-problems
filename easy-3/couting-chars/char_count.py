'''A module for counting characters in Strings'''

def char_count(phrase):
    non_space_phrase = phrase.replace(' ', '')

    return len(non_space_phrase)

