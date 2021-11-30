'''A module for working with lists of integers'''

ENGLISH_WORDS = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen',
}
NUMS_FROM_WORDS = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
    'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
    'eighteen': 18, 'nineteen': 19,
}

def alphabetic_number_sort(nums):
    '''
    Sort a list of input integers by their English counterpart
    and return a new sorted list
    '''
    english_words = [ENGLISH_WORDS.get(num) for num in nums]
    english_words.sort()
    nums_by_eng_word = [NUMS_FROM_WORDS.get(word) for word in english_words]
    return nums_by_eng_word
