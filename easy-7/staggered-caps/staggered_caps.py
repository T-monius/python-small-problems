'''A module for manipulating case of string characters'''

def staggered_caps(normal_case, staggered=''):
    '''Return a string with the even indexed charaters of the input
       string upper cased'''
    idx = len(staggered)
    if idx == len(normal_case):
        return staggered

    char = normal_case[idx]
    char = char.upper() if idx % 2 == 0 else char.lower()

    staggered += char

    return staggered_caps(normal_case, staggered)
