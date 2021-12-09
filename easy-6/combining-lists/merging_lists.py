'''A module for working with multiple lists'''

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

    while idx_one < len(l_one):
        val1 = l_one[idx_one]
        if seen.get(val1, False):
            idx_one += 1
            continue

        combined.append(val1)
        seen[val1] = True

        idx_one += 1

    while idx_two < len(l_two):
        val2 = l_two[idx_two]
        if seen.get(val2, False):
            idx_two += 1
            continue

        combined.append(val2)
        seen[val2] = True

        idx_two += 1

    return combined
