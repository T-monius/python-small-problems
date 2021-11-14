'''A module for string to integer conversions'''

INTEGERS_FROM_STRING_DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

def string_to_integer(int_str):
    total = 0
    end_idx  = len(int_str) - 1
    index_multiplier = 0

    while end_idx >= 0:
        current_char = int_str[end_idx]
        num = INTEGERS_FROM_STRING_DIGITS[current_char]
        multiplier = 10 ** index_multiplier
        total += (num * multiplier)
        end_idx -= 1
        index_multiplier += 1

    return total