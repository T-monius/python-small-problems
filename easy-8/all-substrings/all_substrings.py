'''A module for retrieving substrings from a target string'''

def substrings(target):
    '''Return a list of substrings ordered by the position of the
       beginning character in the substring where position is based
       on incrementing indexes from 0 to the end of the string'''
    target_len = len(target)
    idx = 0
    all_substrings = []
    if target_len < 1:
        return all_substrings

    while idx < target_len:
        upto_idx = idx + 1
        while upto_idx <= target_len:
            current_substring = target[idx:upto_idx]
            all_substrings.append(current_substring)
            upto_idx += 1
        idx += 1

    return all_substrings
