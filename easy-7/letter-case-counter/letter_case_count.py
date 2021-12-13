'''A module for analyzing strings'''
import re

IS_LOWER = re.compile(r'[a-z]')
IS_UPPER = re.compile(r'[A-Z]')

def letter_case_count(str_input):
    '''Return a dictionary containing count of upper, lowercase letters
       as well as those that are neither'''
    case_count = { 'lowercase': 0, 'uppercase': 0, 'neither': 0}

    for char in str_input:
        if IS_LOWER.match(char):
            case_count['lowercase'] += 1
            continue
        if IS_UPPER.match(char):
            case_count['uppercase'] += 1
            continue
        case_count['neither'] += 1

    return case_count
