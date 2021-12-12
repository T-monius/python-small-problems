'''A module for combining two lists'''

def interleave(primary, secondary):
    '''Combine to lists by alternating elements'''
    interleaved = []
    idx = 0

    for primary_element in primary:
        interleaved.append(primary_element)
        secondary_element = secondary[idx]
        interleaved.append(secondary_element)
        idx += 1

    return interleaved
