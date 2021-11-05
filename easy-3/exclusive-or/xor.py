'''A module for determining an exclusive OR condition'''

def is_xor(val, val1):
    """
    Determine if one and only one of the input arguments
    evaluates to True.
    """
    if val:
        if not val1:
            return True
    if val1:
        if not val:
            return True

    return False