'''A module for working with words that are written from spelling
   blocks'''

BLOCK_LETTER_DICT = {
    'A':'N',
    'N':'A',
    'B':'O',
    'O':'B',
    'C':'P',
    'D':'Q',
    'E':'R',
    'R':'E',
    'F':'S',
    'S':'F',
    'G':'T',
    'T':'G',
    'H':'U',
    'U':'H',
    'I':'V',
    'V':'I',
    'J':'W',
    'W':'J',
    'X':'K',
    'K':'X',
    'L':'Y',
    'Y':'L',
    'Z':'M',
    'M':'Z',
}

def is_block_word(word):
    '''Return whether a word can be spelled from spelling blocks
       which contain a pair of letters. A pair can be used just once'''
    seen_letters = set()

    for letter in word.upper():
        pair_letter = BLOCK_LETTER_DICT[letter]
        if letter in seen_letters or pair_letter in seen_letters:
            return False

        seen_letters.add(letter)
        seen_letters.add(pair_letter)

    return True
