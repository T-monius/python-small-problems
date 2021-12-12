'''A module for working with multiple lists'''

def add_remaining_unseen_values_to_combined(lst, combined, seen, idx):
    while idx < len(lst):
        val = lst[idx]
        if seen.get(val, False):
            idx += 1
            continue

        combined.append(val)
        seen[val] = True

        idx += 1

def uniq_combine(l_one, l_two):
    '''Combine two lists of arbitrary elements w/o duplicates'''
    seen = {}
    combined = []
    idx_one = 0
    idx_two = 0

    while idx_one < len(l_one) and idx_one < len(l_two):
        val1 = l_one[idx_one]
        val2 = l_two[idx_two]

        if seen.get(val1, False):
            idx_one += 1
            continue
        if seen.get(val2, False):
            idx_two += 1
            continue

        combined.append(val1)
        seen[val1] = True

        combined.append(val2)
        seen[val2] = True

        idx_one += 1
        idx_two += 1

    add_remaining_unseen_values_to_combined(l_one, combined, seen, idx_one)
    add_remaining_unseen_values_to_combined(l_two, combined, seen, idx_two)

    return combined
