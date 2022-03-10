'''A module for rotating the elements of a list'''

def rotate_list(lst):
    '''Rotate an input integer by moving the first digit at the zeroeth
       index to the last index'''
    if len(lst) < 2:
        return lst

    rotated = lst[1:] + [lst[0]]

    return rotated

def rotate_rightmost_digits(num, n):
    '''Rotate a number by the number of digits indicated by the second
       argument n from the right'''
    digit_chars = list(str(num))
    max_index = len(digit_chars) - n
    prefix = digit_chars[0:max_index]
    suffix = digit_chars[-n:]
    rotated_chars = prefix + rotate_list(suffix)
    new_num_str = ''.join(rotated_chars)

    return int(new_num_str)
