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

def alpha_staggered_caps(normal_case, alpha_staggered='', alpha_count=0):
    '''Return a string with every other alhpa charater of the input
       string upper cased'''
    idx = len(alpha_staggered)
    if idx == len(normal_case):
        return alpha_staggered

    char = normal_case[idx]
    if char.isalpha():
        alpha_count += 1
        char = char.upper() if alpha_count % 2 == 1 else char.lower()

    alpha_staggered += char

    return alpha_staggered_caps(normal_case, alpha_staggered, alpha_count)
