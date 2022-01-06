'''A module for working with palindromes'''

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


def is_palindrome(target):
    '''Deterine if a target string is a palindrome'''
    if len(target) < 2:
        return False

    lst = list(target)
    reversed_lst = list(reversed(lst))

    equality = reversed_lst == lst

    return equality


def is_palindromic(some_string):
    '''Deterine if a target string is a palindrome iteratively'''
    if len(some_string) < 2:
        return False

    anchor = 0
    end_idx = len(some_string) - 1

    while anchor < end_idx:
        char = some_string[anchor]
        char1 = some_string[end_idx]

        if char != char1:
            return False

        anchor += 1
        end_idx -= 1

    return True


def palindromes(target):
    '''Return a list of all palindromes found among all substrings
       of a target'''
    all_substrings = substrings(target)
    found_palindromes = list(filter(is_palindromic, all_substrings))

    return found_palindromes
