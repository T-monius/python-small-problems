'''A module for transforming strings'''

def word_cap(phrase):
    '''Capitalize words in a phrase except if the first character is
       non-alpha'''
    cap_words = []
    for word in phrase.split():
        if word[0].isalpha():
            cap_words.append(word.title())
            continue

        cap_words.append(word)

    return ' '.join(cap_words)
