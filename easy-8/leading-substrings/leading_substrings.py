'''A module for finding substrings'''

def leading_substrings(target, idx=1, strs=None):
    '''Return all substrings of a target from beginning'''
    if strs is None:
        strs = []
    if len(target) < 1 or idx > len(target):
        return strs

    strs.append(target[:idx])

    return leading_substrings(target, idx + 1, strs)
