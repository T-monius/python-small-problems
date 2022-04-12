'''A module to implement the bubble sort algorithm'''

def sort_the_bubble_way(values):
    '''Sort the input list in place and return'''
    passes = 0
    swaps = None

    while passes < 1 or swaps > 0:
        swaps = 0
        next_val = None
        for idx, val in enumerate(values):
            if idx < len(values) - 1:
                next_val = values[idx + 1]
            if next_val and (val > next_val):
                swaps += 1
                values[idx], values[idx + 1] = values[idx + 1], values[idx]

        passes += 1

    return values
