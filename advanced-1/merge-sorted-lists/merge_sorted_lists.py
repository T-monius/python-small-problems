'''A module for merging lists'''

def merge(vals, other_vals):
    '''Return a new list formed by merging all elements of two input
       lists that are assumed to be sorted without sorting or mutating
       either input list. The merged list maintains ordering.'''
    len_vals = len(vals)
    len_other = len(other_vals)
    new_len = len(vals) + len(other_vals)
    merged = []
    idx = 0
    other_idx = 0

    for _ in range(0, new_len):
        if idx < len_vals and other_idx < len_other:
            element = vals[idx]
            other_el = other_vals[other_idx]
            if element < other_el:
                merged.append(element)
                idx += 1
            else:
                merged.append(other_el)
                other_idx += 1
            continue
        if idx >= len_vals:
            other_el = other_vals[other_idx]
            merged.append(other_el)
            other_idx += 1
        else:
            element = vals[idx]
            merged.append(element)
            idx += 1


    return merged
