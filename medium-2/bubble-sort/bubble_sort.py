'''A module to implement the bubble sort algorithm'''

def pass_over_values_swapping_in_place(values, swaps):
    '''Make a pass over values swapping consecutive values where the
       predecessor is greater than the successor counting swaps as
       they occur. Return the count of swaps that occurred during the
       pass.'''
    limit = len(values) - 1
    for idx in range(0, limit):
        val = values[idx]
        next_val = values[idx + 1]
        if val > next_val:
            swaps += 1
            values[idx], values[idx + 1] = values[idx + 1], values[idx]

    return swaps


def sort_the_bubble_way_in_place(values):
    '''Sort the input list in place and return'''
    passes = 0
    swaps = None

    while passes < 1 or swaps > 0:
        swaps = 0
        swaps = pass_over_values_swapping_in_place(values, swaps)

        passes += 1

    return values
