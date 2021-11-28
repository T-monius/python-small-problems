'''A module for dealing with strings'''

def cleanup(phrase):
    '''Remove non-alpha chararters from a str'''
    non_alphas = ''

    for char in phrase:
        if char.isalpha():
            non_alphas += char
        else:
            if not non_alphas or non_alphas[-1] != ' ':
                non_alphas += ' '

    return non_alphas