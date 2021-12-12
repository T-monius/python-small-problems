'''A module for working halves of lists'''

def slice_in_half(whole):
    '''Return two halves of an input array'''
    middle_idx = int(len(whole) / 2)
    is_odd_len = len(whole) % 2 != 0

    if is_odd_len:
        middle_idx += 1

    return [whole[:middle_idx], whole[middle_idx:]]
