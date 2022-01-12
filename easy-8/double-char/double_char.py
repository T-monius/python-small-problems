'''A module for working with string characters and doubling them'''

VOWELS = { 'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
           'A': True, 'E': True, 'I': True, 'O': True, 'U': True }

def repeater(target):
    '''Double all cahracters of an input string and return the
       doubling'''
    doubled = []

    for char in target:
        doubled.append(char * 2)

    return ''.join(doubled)


def double_consonants(target):
    '''Double only the consonant characters of target string and
       return'''
    doubled = []

    for char in target:
        if char.isalpha():
            if not VOWELS.get(char):
                doubled.append(char * 2)
                continue

        doubled.append(char)

    return ''.join(doubled)
