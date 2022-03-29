'''A module to calculate percentages of occurrences of types of
   characters in text'''

CASE_TYPES = ['lowercase', 'uppercase', 'neither']

def calculate_percentage(num, other_num):
    '''Calculate what percentage of one number is another'''
    return (other_num * 100) / num


def instantiate_counts_for_types(types):
    '''Return a dictionary of counts set to zero for types'''
    counts = {}

    for a_type in types:
        counts[a_type] = 0

    return counts

def percentages_of_type_counts_from_a_total(counts, total, types):
    '''Calculate percentages of each count of a type based on a total'''
    percentages = {}
    for a_type in types:
        percentages[a_type] = calculate_percentage(total, counts[a_type])

    return percentages

def case_finder(char):
    '''Return the case of a character'''
    if char.islower():
        return 'lowercase'
    if char.isupper():
        return 'uppercase'

    return 'neither'


def letter_percentages(text):
    '''Return a dectionary with keys representing the types
       of characters that can be found in an input text where the value
       represents the percentage of the text that contains that key's
       character type'''
    case_counts = instantiate_counts_for_types(CASE_TYPES)

    for letter in text:
        lettercase = case_finder(letter)
        case_counts[lettercase] += 1

    percentages = percentages_of_type_counts_from_a_total(
        case_counts,
        len(text),
        CASE_TYPES,
    )


    return percentages
